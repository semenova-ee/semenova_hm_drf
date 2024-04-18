from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets

from members.models import Payment
from members.serializers import PaymentSerializer
from members.services import get_session
from .filters import PaymentFilter
from .models import Course, Lesson
from .paginators import CustomPageNumberPagination
from .serializers import CourseSerializer, LessonSerializer
from members.permissions import IsModerator, IsOwner, IsAuthenticated, PermissionPolicyMixin
from materials.tasks import send_update_course

class CourseViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes_per_method = {
        "list": [IsOwner | IsModerator],
        "retrieve": [IsOwner | IsModerator],
        "update": [IsOwner | IsModerator],
        "partial_update": [IsOwner | IsModerator],
        "create": [IsAuthenticated & ~IsModerator],
        "destroy": [IsOwner & IsAuthenticated]
    }

    pagination_class = CustomPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        updated_course = serializer.save()
        send_update_course.delay(updated_course.course.id)


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPageNumberPagination


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner | IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner | IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]


class PaymentViewSet(viewsets.ModelViewSet):
    """ViewSet for payment"""
    queryset = Payment.objects.all()

    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter
    ordering_fields = ['payment_date']
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        paid_of_course = serializer.save()
        stripe_obj = get_session(paid_of_course)
        paid_of_course.stripe_link = stripe_obj.url
        paid_of_course.stripe_id = stripe_obj.id
        paid_of_course.save()
