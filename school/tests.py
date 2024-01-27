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
        pass

    def test_create_lesson(self):
        """Create Lesson"""
        data = {
            "title": "test lesson",
            "description": "test description",
            "url": "https://my.sky.pro/student-cabinet/stream-lesson/52714/theory/7",
        }

        response = self.client.post(
            "/lesson/create/",
            data=data,
            format='json'
        )
        # print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'title': 'test lesson', 'description': 'test description', 'image': None,
             'url': 'https://my.sky.pro/student-cabinet/stream-lesson/52714/theory/7', 'course': None, 'owner': None}

        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_read_lesson(self):
        """Read Lesson"""
        data = {
            "title": "test lesson",
            "description": "test description",
            "url": "https://my.sky.pro/student-cabinet/stream-lesson/52714/theory/7",
        }

        response = self.client.get(
            "/lesson/",
            data=data,
            format='json'
        )
        #print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertFalse(
            Lesson.objects.all().exists()
        )

    def test_update_lesson(self):
        """Update Lesson"""
        data = {
            "title": "test lesson",
            "description": "test description",
            "url": "https://my.sky.pro/student-cabinet/stream-lesson/52714/theory/7",
        }

        response = self.client.get(
            "/lesson/",
            data=data,
            format='json'
        )
        # print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertFalse(
            Lesson.objects.all().exists()
        )

    def test_destroy_lesson(self):
        """Update Lesson"""
        data = {
            "title": "test lesson",
            "description": "test description",
            "url": "https://my.sky.pro/student-cabinet/stream-lesson/52714/theory/7",
        }

        response = self.client.delete(
            "/lesson/delete/1/",
            data=data,
            format='json'
        )
        # print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND)
        self.assertFalse(
            Lesson.objects.all().exists()
        )


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
