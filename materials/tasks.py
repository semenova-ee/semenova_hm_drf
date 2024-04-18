from celery import shared_task
from django.core.mail import send_mail
from education_course import settings
from materials.models import Course
from members.models import CourseSubscription


@shared_task
def send_update_course(course_id):
    course = Course.objects.get(pk=course_id)
    course_sub = CourseSubscription.objects.filter(course=course_id)
    for sub in course_sub:
        send_mail(subject=f"{course.title}",
                  message=f"Обновление {course.title}",
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[f'{sub.user.email}'],
                  fail_silently=True
                  )