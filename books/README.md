# 📚 Book App - Library Management System API

## 📖 Overview

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

## 📂 Models

The `Book` model contains the following fields:

```python
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    available_copies = models.PositiveIntegerField(default=1)
```

## 🔗 API Endpoints

| Method | Endpoint           | Description              | Permissions |
| ------ | ------------------ | ------------------------ | ----------- |
| GET    | `/api/books/`      | Retrieve all books       | Everyone    |
| POST   | `/api/books/`      | Add a new book           | Admin only  |
| GET    | `/api/books/{id}/` | Retrieve a specific book | Everyone    |
| PUT    | `/api/books/{id}/` | Update a book            | Admin only  |
| DELETE | `/api/books/{id}/` | Delete a book            | Admin only  |

## 🔍 Filtering Books

You can filter books using query parameters:

```
GET /api/books/?title=Harry Potter
GET /api/books/?author=J.K. Rowling
GET /api/books/?available=true
```

## 🔑 Permissions

- **Admin Users (****`is_staff=True`****)** can create, update, and delete books.
- **Regular Users** can only view books.

## 🔧 Installation & Setup

1. **Run Migrations:**
   ```bash
   python manage.py makemigrations books
   python manage.py migrate
   ```
2. **Run Development Server:**
   ```bash
   python manage.py runserver
   ```
3. **Test API using Postman **
