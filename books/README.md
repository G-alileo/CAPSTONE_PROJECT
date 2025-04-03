# 📚 Book App - Library Management System API

## 📚 Overview

The **Book App** is a core component of the **Library Management System API**, responsible for managing book-related functionalities such as creating, updating, deleting, and listing books. This app provides a RESTful API built with Django REST Framework (DRF) that allows users and administrators to interact with the book catalog.

## 🚀 Features

- **CRUD Operations:**
  - 📌 Create books (**Admin only**)
  - 📌 Retrieve all books
  - 📌 Update book details (**Admin only**)
  - 📌 Delete books (**Admin only**)
- **Filtering & Search:**
  - 🔍 Filter books by title, author, and availability
- **Permissions:**
  - ✅ Admins can manage books (Add, Edit, Delete)
  - ✅ All users can view books
- **Book Checkout & Return System:**
  - ✅ Users can borrow books if copies are available
  - ✅ Users must return borrowed books before borrowing again
  - ✅ Availability updates when a book is borrowed or returned

## 🐂 Models

The `Book` model contains the following fields:

```python
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    available_copies = models.PositiveIntegerField(default=1)
```

The `Transaction` model tracks book checkouts and returns:

```python
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
```

## 🔗 API Endpoints

| Method | Endpoint                   | Description              | Permissions         |
| ------ | -------------------------- | ------------------------ | ------------------- |
| GET    | `/api/books/`              | Retrieve all books       | Everyone            |
| POST   | `/api/books/`              | Add a new book           | Admin only          |
| GET    | `/api/books/{id}/`         | Retrieve a specific book | Everyone            |
| PUT    | `/api/books/{id}/`         | Update a book            | Admin only          |
| DELETE | `/api/books/{id}/`         | Delete a book            | Admin only          |
| POST   | `/api/checkout/{book_id}/` | Check out a book         | Authenticated Users |
| POST   | `/api/return/{book_id}/`   | Return a borrowed book   | Authenticated Users |

## 🔍 Filtering Books

You can filter books using query parameters:

```
GET /api/books/?title=Atomic Habits
GET /api/books/?author=john doe
GET /api/books/?available=true
```

## 🔑 Permissions

- **Admin Users (****`is_staff=True`****)** can create, update, and delete books.
- **Regular Users** can only view books and borrow/return books.

##

