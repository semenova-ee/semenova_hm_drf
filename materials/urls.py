from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import MaterialsConfig
from .views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, PaymentViewSet

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register('payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
    path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
]
