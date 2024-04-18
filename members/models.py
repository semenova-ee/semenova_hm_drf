from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


NULLABLE = {'blank': True, 'null': True}


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    course = models.ForeignKey('materials.Course', related_name='course_payments', on_delete=models.CASCADE,
                               null=True, blank=True)
    lesson = models.ForeignKey('materials.Lesson', related_name='lesson_payments', on_delete=models.CASCADE,
                               null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[('cash', 'Наличные'), ('transfer', 'Перевод')])
    stripe_link = models.URLField(max_length=400, **NULLABLE)
    stripe_id = models.CharField(max_length=255, **NULLABLE)


    def __str__(self):
        return f"{self.user} - {self.date} - {self.amount} - {self.payment_method}"


class CourseSubscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey('materials.Course', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'course']
        verbose_name = _('Course Subscription')
        verbose_name_plural = _('Course Subscriptions')

    def __str__(self):
        return f"{self.user.username} subscribed to {self.course.title}"
