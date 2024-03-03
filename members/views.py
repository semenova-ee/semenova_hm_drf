from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from materials.models import Course
from rest_framework.filters import OrderingFilter
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payment, CustomUser, CourseSubscription
from .serializers import PaymentSerializer, UserSerializer, CourseSubscriptionSerializer
from .filters import PaymentFilter


class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PaymentFilter
    ordering_fields = ['date']  # Define fields for ordering


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class CourseSubscriptionAPIView(APIView):
    serializer_class = CourseSubscriptionSerializer

    def post(self, request, *args, **kwargs):
        # Получаем пользователя и ID курса из запроса
        user = request.user
        course_id = request.data.get('course_id')
        course = get_object_or_404(Course, id=course_id)

        # Проверяем, существует ли уже подписка пользователя на данный курс
        subscription_exists = CourseSubscription.objects.filter(user=user, course=course).exists()

        # Если подписка существует, удаляем ее, иначе создаем новую
        if subscription_exists:
            CourseSubscription.objects.filter(user=user, course=course).delete()
            message = 'Subscription removed'
        else:
            CourseSubscription.objects.create(user=user, course=course)
            message = 'Subscription added'

        return Response({"message": message})
