from django.db import models


from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_payment = models.DateField()
    course = models.ForeignKey('materials.Course', related_name='course_payments', on_delete=models.CASCADE,
                               null=True, blank=True)
    lesson = models.ForeignKey('materials.Lesson', related_name='lesson_payments', on_delete=models.CASCADE,
                               null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[('cash', 'Наличные'), ('transfer', 'Перевод')])

    def __str__(self):
        return f"{self.user} - {self.date} - {self.amount} - {self.payment_method}"


