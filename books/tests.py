from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Transaction
from django.utils.timezone import now


# Create your tests here.

User = get_user_model()

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            isbn="1234567890123",
            published_date="2024-01-01",
            copies_available=5
        )

    def test_book_creation(self):
        self.assertEqual(str(self.book), "Test Book")
        self.assertEqual(self.book.isbn, "1234567890123")
        self.assertEqual(self.book.copies_available, 5)


class TransactionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.book = Book.objects.create(title="Test Book", author="Author", isbn="9876543210987", published_date="2024-01-01", copies_available=5)
        
    def test_transaction_creation(self):
        transaction = Transaction.objects.create(user=self.user, book=self.book)
        self.assertEqual(str(transaction), "testuser borrowed Test Book")
        self.assertIsNone(transaction.return_date)


class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.admin = User.objects.create_superuser(username="admin", email="admintester@example.com", password="adminpass")
        self.book = Book.objects.create(title="Test Book", author="Author", isbn="9876543210987", published_date="2024-01-01", copies_available=5)

    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_create_book(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post("/api/books/", {
            "title": "New Book",
            "author": "Jane Doe",
            "isbn": "1231231231231",
            "published_date": "2024-01-01",
            "copies_available": 10
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TransactionAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.book = Book.objects.create(title="Test Book", author="Author", isbn="9876543210987", published_date="2024-01-01", copies_available=1)
        self.client.force_authenticate(user=self.user)
    
    def test_checkout_book(self):
        response = self.client.post(f"/api/checkout/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.book.refresh_from_db()
        self.assertEqual(self.book.copies_available, 0)
    
    def test_return_book(self):
        transaction = Transaction.objects.create(user=self.user, book=self.book, checkout_date=now())
        response = self.client.post(f"/api/return/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        transaction.refresh_from_db()
        self.assertIsNotNone(transaction.return_date)
