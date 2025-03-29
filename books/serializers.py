from rest_framework import serializers
from .models import Book, Transaction

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields in the API response

    def validate_isbn(self, value):
        """Ensure ISBN is unique"""
        if Book.objects.filter(isbn=value).exists():
            raise serializers.ValidationError("A book with this ISBN already exists.")
        return value

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'book', 'checkout_date', 'return_date']