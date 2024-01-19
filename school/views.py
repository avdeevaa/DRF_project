from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.shortcuts import render
from rest_framework import viewsets, generics

from school.models import Course, Lesson, Payments
from school.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer


class CourseViewSet(viewsets.ModelViewSet):  # ViewSet
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIview(generics.CreateAPIView):  # generics
    serializer_class = LessonSerializer


class LessonListAPIview(generics.ListAPIView):  # generics
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIview(generics.RetrieveAPIView):  # generics
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIview(generics.UpdateAPIView):  # generics
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIview(generics.DestroyAPIView):  # generics
    queryset = Lesson.objects.all()  # only queryset


class PaymentsListAPIview(generics.ListAPIView):  # generics
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course_paid', 'lesson_paid', 'payment_method')
    ordering_fields = ('payment_date',)
