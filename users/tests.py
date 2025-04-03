from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserTests(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username="admin", email="admin@example.com", password="adminpass")
        self.regular_user = User.objects.create_user(username="user", email="user@example.com", password="userpass")
        self.admin_token = Token.objects.create(user=self.admin_user)
        self.user_token = Token.objects.create(user=self.regular_user)
        self.register_url = "/api/users/register/"
        self.login_url = "/api/users/login/"
        self.users_url = "/api/users/users/"

    def test_register_user_successfully(self):
        data = {"username": "testuser", "email": "test@example.com", "password": "Test@1234", "confirm_password": "Test@1234"}
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_user_password_mismatch(self):
        data = {"username": "testuser", "email": "test@example.com", "password": "Test@1234", "confirm_password": "WrongPass"}
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_duplicate_username(self):
        data = {"username": "user", "email": "newuser@example.com", "password": "Test@1234", "confirm_password": "Test@1234"}
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_successful(self):
        data = {"username": "user", "password": "userpass"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_invalid_credentials(self):
        data = {"username": "user", "password": "wrongpass"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_admin_can_get_user_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token.key}')
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_regular_user_cannot_get_user_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_token.key}')
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_delete_user(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token.key}')
        response = self.client.delete(f"{self.users_url}{self.regular_user.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
