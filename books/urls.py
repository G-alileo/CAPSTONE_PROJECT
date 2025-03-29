from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)  # Registers all book-related routes

urlpatterns = [
    path('', include(router.urls)),
    path('checkout/<int:book_id>/', TransactionViewSet.as_view({'post': 'checkout_book'}), name='checkout-book'),
    path('return/<int:book_id>/', TransactionViewSet.as_view({'post': 'return_book'}), name='return-book'),

]
