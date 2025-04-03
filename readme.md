# Django Library Management System API

## 📌 Project Overview

This is a **Django REST Framework (DRF) API** for a **Library Management System (LMS)** that allows users to:

- **Authenticate** (Register, Login, Token-based Auth)
- **Manage Books** (CRUD, Filtering, Search)
- **Borrow & Return Books** (Transaction System)
- **Manage Users** (Admin Controls)



---

## 🚀 Features

### 🔑 Authentication

- **User Registration & Login** (Token-based authentication)
- **User Profiles**
- **Admin & User Roles**

### 📚 Book Management

- **CRUD Operations** (Admins can create, update, delete books)
- **View Available Books**
- **Search & Filtering by Title, Author, and Availability**

### 📖 Book Transactions

- **Users can borrow (checkout) books**
- **Users can return books**
- **Transaction history for users**

### 👤 User Management

- **Admins can manage users**
- **Admins can delete users**

---

## 📂 Project Structure

```
library_management/
│── books/              # Books app (CRUD, Filtering, Transactions)
│── users/              # User authentication & management
│── library_management/ # Main Django settings and configurations
│── requirements.txt    # Dependencies
│── manage.py           # Django project manager
```

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/G-alileo/CAPSTONE_PROJECT.git
cd CAPSTONE_PROJECT
```

### 2️⃣ Create a Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3️⃣ Apply Migrations & Create Superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4️⃣ Run the Development Server

```bash
python manage.py runserver
```

---

## 🔑 Authentication

### 1️⃣ Register

**Endpoint:** `/api/register/`

```json
{
    "username": "testuser",
    "password": "securepassword"
}
```

**Response:**

```json
{
    "token": "abcd1234token"
}
```

### 2️⃣ Login

**Endpoint:** `/api/login/`

```json
{
    "username": "testuser",
    "password": "securepassword"
}
```

**Response:**

```json
{
    "token": "abcd1234token"
}
```

---

## 📚 Books API

### 1️⃣ Get All Books

**Endpoint:** `GET /api/books/`

### 2️⃣ Search Books by Title or Author

**Endpoint:** `GET /api/books/?title=harry&author=rowling`

### 3️⃣ Admin: Create a Book

**Endpoint:** `POST /api/books/`

```json
{
    "title": "Django for Beginners",
    "author": "William S. Vincent",
    "isbn": "1234567890123",
    "published_date": "2022-01-01",
    "copies_available": 5
}
```

### 4️⃣ Get a Single Book

**Endpoint:** `GET /api/books/{book_id}/`

### 5️⃣ Admin: Update a Book

**Endpoint:** `PUT /api/books/{book_id}/`

### 6️⃣ Admin: Delete a Book

**Endpoint:** `DELETE /api/books/{book_id}/`

---

## 📖 Transactions API

### 1️⃣ Checkout a Book

**Endpoint:** `POST /api/checkout/{book_id}/`

```json
{
    "user_id": 1
}
```

### 2️⃣ Return a Book

**Endpoint:** `POST /api/return/{book_id}/`

### 3️⃣ Get User Transactions

**Endpoint:** `GET /api/transactions/`

---

## 👤 User Management API

### 1️⃣ Get User Details (Admin only)

**Endpoint:** `GET /api/users/{user_id}/`

### 2️⃣ Admin: Delete a User

**Endpoint:** `DELETE /api/users/{user_id}/`

---

## 🛠 Tech Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** Token-based authentication
- **Database:** sqlite3(Production),  (



---

## 📄 License

This project is **MIT Licensed**.

---

##
