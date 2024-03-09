from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from members.models import CustomUser
from .models import Lesson, Course

class LessonCRUDTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

        # Create a course
        self.course = Course.objects.create(title='Test Course', description='Test Course Description', owner=self.user)

        # Create lessons associated with the course
        self.lesson1 = Lesson.objects.create(title='Lesson 1', description='Description 1', video_link='https://www.youtube.com', course=self.course, owner=self.user)
        self.lesson2 = Lesson.objects.create(title='Lesson 2', description='Description 2', video_link='https://www.youtube.com', course=self.course, owner=self.user)

        # Authenticate the client
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_lessons(self):
        response = self.client.get('/api/materials/lessons/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)  # Assuming there are 2 lessons in the database

    def test_retrieve_lesson(self):
        response = self.client.get(f'/api/materials/lessons/{self.lesson1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Lesson 1')

    def test_create_lesson(self):
        data = {
            'title': 'New Lesson',
            'description': 'New Description',
            'video_link': 'https://www.youtube.com',
            'course': self.course.id,  # Associate the lesson with the course
            'owner': self.user.id  # Assign the lesson owner
        }
        response = self.client.post('/api/materials/lessons/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 3)  # Assuming one lesson was created

    def test_update_lesson(self):
        data = {
            'title': 'Updated Lesson',
            'description': 'Updated Description',
            'video_link': 'https://www.youtube.com',
            'course': self.course.id,
            'owner': self.user.id
        }
        response = self.client.put(f'/api/materials/lessons/{self.lesson1.id}/update/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson1.refresh_from_db()
        self.assertEqual(self.lesson1.title, 'Updated Lesson')

    def test_delete_lesson(self):
        response = self.client.delete(f'/api/materials/lessons/{self.lesson1.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 1)  # Assuming one lesson was deleted
