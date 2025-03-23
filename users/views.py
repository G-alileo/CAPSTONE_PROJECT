from rest_framework import generics, permissions, viewsets, status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid Credentials"}, status=400)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can manage users

    def destroy(self, request, *args, **kwargs):
        """Allow admins to delete users"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    # def get_queryset(self):
    #     """Ensure admins can view all users"""
    #     if self.request.user.is_staff:  # Only return users if the requester is an admin
    #         return User.objects.all()
    #     return User.objects.none()  # Return empty list if not admin