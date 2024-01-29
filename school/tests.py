from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Lesson, Course, Subscription
from users.models import User

from school.models import Subscription
from .serializers import SubscriptionSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class LessonTestCase(APITestCase):

    def setUp(self):
        self.lesson_data = {
            "title": "test lesson",
            "description": "test description",
            "url": "https://my.sky.pro/student-cabinet/stream-lesson/52714/theory/7",
        }
        self.lesson = Lesson.objects.create(**self.lesson_data)

    def test_create_lesson(self):
        response = self.client.post("/lesson/create/", data=self.lesson_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            'id': 2,  # Проверьте, что возвращается правильный id урока
            'title': 'test lesson',
            'description': 'test description',
            'image': None,  # Добавлен ключ 'image'
            'url': 'https://my.sky.pro/student-cabinet/stream-lesson/52714/theory/7',
            'course': None,
            'owner': None
        })
        self.assertTrue(Lesson.objects.filter(title='test lesson').exists())

    def test_read_lesson(self):
        response = self.client.get("/lesson/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Lesson.objects.filter(title='test lesson').exists())

    def test_update_lesson(self):
        updated_data = {
            "title": "updated lesson",
            "description": "updated description",
            "url": "https://my.sky.pro/student-cabinet/stream-lesson/52714/theory/8",
        }
        response = self.client.put(f"/lesson/update/{self.lesson.id}/", data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, 'updated lesson')
        self.assertEqual(self.lesson.description, 'updated description')
        self.assertEqual(self.lesson.url, 'https://my.sky.pro/student-cabinet/stream-lesson/52714/theory/8')

    def test_destroy_lesson(self):
        response = self.client.delete(f"/lesson/delete/{self.lesson.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(title='test lesson').exists())


#  SECOND PART
class SubscriptionAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test_user@example.com')
        self.course = Course.objects.create(title='Test Course', description='Test Description')
        self.subscription_data = {'user': self.user.id, 'course': self.course.id, 'subscription': True}

    def test_create_subscription(self):
        url = '/subscr/create/'
        response = self.client.post(url, self.subscription_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.count(), 1)
        self.assertEqual(Subscription.objects.get().user, self.user)
        self.assertEqual(Subscription.objects.get().course, self.course)

    def test_update_subscription(self):
        subscription = Subscription.objects.create(user=self.user, course=self.course)
        url = f'/subscr/update/{subscription.id}/'
        updated_subscription_data = {'user': self.user.id, 'course': self.course.id, 'subscription': False}
        response = self.client.put(url, updated_subscription_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.get(id=subscription.id).subscription, False)

    def test_delete_subscription(self):
        subscription = Subscription.objects.create(user=self.user, course=self.course)
        url = f'/subscr/delete/{subscription.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscription.objects.count(), 0)
