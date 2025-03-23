# Users App - Library Management System API

## Overview

The `users` app is responsible for managing user authentication and registration in the Library Management System API. This includes user registration, login, and authentication using Django's built-in authentication system with token authentication.

## Deliverables

### 1. **User Authentication System**

- Implemented a custom `User` model extending Django's `AbstractUser`.
- Added fields: `email`, `date_of_membership`, `is_active`, and `role` (admin/user).
- Configured `AUTH_USER_MODEL` to use the custom User model.

### 2. **User Registration**

- Created an endpoint `/api/users/register/` to allow new users to sign up.
- Users provide a `username`, `email`, `password`, and `role`.
- Ensured password validation and confirmation.

### 3. **User Login**

- Implemented an endpoint `/api/users/login/`.
- Users authenticate with `username` and `password`.
- Returns an authentication token upon successful login.

### 4. **Authentication System**

- Integrated Django REST Framework’s Token Authentication.
- Configured authentication in `settings.py`.
- Users must provide a valid token to access protected endpoints.

## API Endpoints

| Endpoint     | Method | Description                            |
| ------------ | ------ | -------------------------------------- |
| `/register/` | POST   | Register a new user                    |
| `/login/`    | POST   | Login and receive authentication token |

## Setup and Usage

1. Run migrations:
   ```bash
   python manage.py makemigrations users
   python manage.py migrate
   ```
2. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```
3. Start the server:
   ```bash
   python manage.py runserver
   ```
4. Test authentication using Postman or cURL.

## Next Steps

- Implement user management features for the admin role.
- Add user profile management functionalities.
- Improve authentication with JWT in future updates.

---

This completes the authentication system and Week 1 objective.

