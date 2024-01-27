from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from school.models import Course, Lesson, Payments, Subscription
from school.paginators import LessonPagination, CoursePagination
from school.permissions import IsOwner
from school.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer, SubscriptionSerializer


class CourseViewSet(viewsets.ModelViewSet):  # ViewSet
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = CoursePagination


class LessonCreateAPIview(generics.CreateAPIView):  # generics
    serializer_class = LessonSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    # def perform_create(self, serializer):
    #     new_lesson = serializer.save()
    #     new_lesson.owner = self.request.user
    #     new_lesson.save()


class LessonListAPIview(generics.ListAPIView):  # generics
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsAdminUser]
    permission_classes = [AllowAny]
    pagination_class = LessonPagination


class LessonRetrieveAPIview(generics.RetrieveAPIView):  # generics
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsAdminUser, IsOwner]
    permission_classes = [AllowAny]


class LessonUpdateAPIview(generics.UpdateAPIView):  # generics
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner]
    permission_classes = [AllowAny]


class LessonDestroyAPIview(generics.DestroyAPIView):  # generics
    queryset = Lesson.objects.all()  # only queryset
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


class PaymentsListAPIview(generics.ListAPIView):  # generics
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course_paid', 'lesson_paid', 'payment_method')
    ordering_fields = ('payment_date',)
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwner]


class SubscriptionCreateAPIview(generics.CreateAPIView):  # generics
    serializer_class = SubscriptionSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class SubscriptionUpdateAPIview(generics.UpdateAPIView):  # generics
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner]
    permission_classes = [AllowAny]


class SubscriptionDestroyAPIview(generics.DestroyAPIView):  # generics
    queryset = Subscription.objects.all()  # only queryset
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


