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

## 🔗 API Endpoints

- **Base : ip: http://127.0.0.1:8000/**

| Feature         | Method | Endpoint                     | Description |
|----------------|--------|-----------------------------|-------------|
| **Auth**       | POST   | `/api/users/register/`            | User registration |
|               | POST   | `/api/users/login/`               | User login |
| **Books**      | GET    | `/api/books/`               | List all books |
|               | GET    | `/api/books/?title=Atomic Habits&author=John doe` | Search books by title or author |
|               | POST   | `/api/books/`               | Admin: Create a book |
|               | GET    | `/api/books/{book_id}/`     | Retrieve a book |
|               | PUT    | `/api/books/{book_id}/`     | Admin: Update a book |
|               | DELETE | `/api/books/{book_id}/`     | Admin: Delete a book |
| **Transactions** | POST  | `/api/checkout/{book_id}/` | Checkout a book |
|               | POST   | `/api/return/{book_id}/`    | Return a book |
| **Users**      | GET    | `/api/users/users/`    | Admin: Get user details |
|                | GET    | `/api/users/users/{user_id}/`    | Admin: Get user details |
|               | DELETE | `/api/users/users/{user_id}/`    | Admin: Delete a user |

---

## 🛠 Tech Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** Token-based authentication
- **Database:** sqlite3 (Production)

---

## 📄 License

This project is **MIT Licensed**.

---

##

