from django.urls import path
from .views import PaymentListView, UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('users/', UserListCreateAPIView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='users-list'),
]

