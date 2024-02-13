from django.db import models


class Course(models.Model):
    title = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    preview = models.ImageField(upload_to='previews/', null=True, blank=True)


class Lesson(models.Model):
    title = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    preview = models.ImageField(upload_to='previews/', null=True, blank=True)
    video_link = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
