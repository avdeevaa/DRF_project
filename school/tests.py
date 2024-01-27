from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Lesson, Course, Subscription
from users.models import User


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

class SubscriptionTestCase(APITestCase):
    def setUp(self):
        pass

    def test_create_subscription(self):
        """Create Subscription"""
        data = {
            "user": 2,
            "course": 3,
            "subscription": "True",
        }

        response = self.client.post(
            "/subscr/create/",
            data=data,
            format='json'
        )
        print(response.json())
        # self.assertEqual(
        #     response.status_code,
        #     status.HTTP_201_CREATED
        # )

        self.assertEqual(
            response.json(),
            {
                "user": 2,
                "course": 3,
                "subscription": "True",
            }

        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    # def test_update_lesson(self):
    #     """Update Lesson"""
    #     data = {
    #         "title": "test lesson",
    #         "description": "test description",
    #         "url": "https://my.sky.pro/student-cabinet/stream-lesson/52714/theory/7",
    #     }
    #
    #     response = self.client.get(
    #         "/lesson/",
    #         data=data,
    #         format='json'
    #     )
    #     # print(response.json())
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
    #
    #     self.assertFalse(
    #         Lesson.objects.all().exists()
    #     )
    #
    #
    # def test_destroy_lesson(self):
    #     """Update Lesson"""
    #     data = {
    #         "title": "test lesson",
    #         "description": "test description",
    #         "url": "https://my.sky.pro/student-cabinet/stream-lesson/52714/theory/7",
    #     }
    #
    #     response = self.client.delete(
    #         "/lesson/delete/1/",
    #         data=data,
    #         format='json'
    #     )
    #     # print(response.json())
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_404_NOT_FOUND)
    #     self.assertFalse(
    #         Lesson.objects.all().exists()
    #     )
    #
