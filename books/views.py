from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Book, Transaction
from .serializers import BookSerializer, TransactionSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now
from django.db.models import Q

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        """Restrict certain actions to admins only"""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]  # Only admins can modify books
        return [permissions.AllowAny()]  # Anyone can view books
    
    def get_queryset(self):
        """Retrieve books with optional filtering"""
        queryset = Book.objects.all()
        title = self.request.query_params.get('title', None)
        author = self.request.query_params.get('author', None)
        available = self.request.query_params.get('available', None)

        if title:
            queryset = queryset.filter(Q(title__icontains=title))
        if author:
            queryset = queryset.filter(Q(author__icontains=author))
        if available:
            if available.lower() == 'true':
                queryset = queryset.filter(copies_available__gt=0)
            elif available.lower() == 'false':
                queryset = queryset.filter(copies_available=0)

        return queryset
class TransactionViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def checkout_book(self, request, book_id):
        """Allows a user to check out a book if available"""
        book = Book.objects.get(id=book_id)

        if book.copies_available  <= 0:
            return Response({"error": "Book is not available"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if user already has an active transaction for this book
        if Transaction.objects.filter(user=request.user, book=book, return_date__isnull=True).exists():
            return Response({"error": "You have already checked out this book"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new transaction
        transaction = Transaction.objects.create(user=request.user, book=book)
        book.copies_available -= 1
        book.save()

        return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)

    def return_book(self, request, book_id):
        """Allows a user to return a book"""
        try:
            transaction = Transaction.objects.get(user=request.user, book_id=book_id, return_date__isnull=True)
        except Transaction.DoesNotExist:
            return Response({"error": "No active checkout found for this book"}, status=status.HTTP_400_BAD_REQUEST)

        # Mark as returned
        transaction.return_date = now()
        transaction.save()

        # Increase book copies
        book = transaction.book
        book.copies_available  += 1
        book.save()

        return Response({"message": "Book returned successfully"}, status=status.HTTP_200_OK)