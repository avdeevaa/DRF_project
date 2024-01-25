from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from school.models import Course, Lesson, Payments
from school.permissions import IsOwner
from school.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer


class CourseViewSet(viewsets.ModelViewSet):  # ViewSet
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class LessonCreateAPIview(generics.CreateAPIView):  # generics
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIview(generics.ListAPIView):  # generics
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class LessonRetrieveAPIview(generics.RetrieveAPIView):  # generics
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwner]


class LessonUpdateAPIview(generics.UpdateAPIView):  # generics
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonDestroyAPIview(generics.DestroyAPIView):  # generics
    queryset = Lesson.objects.all()  # only queryset
    permission_classes = [IsAuthenticated]


class PaymentsListAPIview(generics.ListAPIView):  # generics
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course_paid', 'lesson_paid', 'payment_method')
    ordering_fields = ('payment_date',)
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwner]
