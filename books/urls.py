from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)  # Registers all book-related routes

urlpatterns = [
    path('', include(router.urls)),
]
