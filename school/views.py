from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from stripe import InvalidRequestError

from school.models import Course, Lesson, Payments, Subscription
from school.paginators import LessonPagination, CoursePagination
from school.permissions import IsOwner
from school.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer, SubscriptionSerializer
import stripe
from django.http import request


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
    # permission_classes = [IsAuthenticated, IsAdminUser, IsOwner]

from django.shortcuts import get_object_or_404

class PaymentsCreateAPIview(generics.CreateAPIView):
    """Создаем эндпоинт для создания платежа"""
    serializer_class = PaymentsSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        stripe.api_key = "sk_test_51OeeJsFwLUbQdeHr078ebwekixI2OAumCmmGC1e0spoY2M9H6eNyuQO0gHSQuC12avF7DqXi4XCgWftsgGGuvn4N00KN2tMZrF"

        amount = request.data.get('amount')
        currency = request.data.get('currency')
        payment_date = request.data.get('payment_date')
        payment_method = request.data.get('payment_method')
        user = request.data.get('user')
        session_id = request.data.get('session_id')
        is_paid = request.data.get('is_paid')
        course_paid = request.data.get('course_paid')
        lesson_paid_id = request.data.get('lesson_paid')

        # lesson_paid = get_object_or_404(Lesson, pk=lesson_paid_id)
        # course_paid_obj = get_object_or_404(Course, pk=course_paid)

        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"],
        )

        # Создание объекта платежа и сохранение в базе данных
        self.perform_create(user, payment_date, amount, currency, payment_method, session_id, is_paid, course_paid, lesson_paid_id)

        return Response({"message": "Payment created successfully."}, status=status.HTTP_201_CREATED)

    def perform_create(self, user, payment_date, amount, currency, payment_method, session_id, is_paid, course_paid, lesson_paid_id):
        Payments.objects.create(
            user=user,
            payment_date=payment_date,
            amount=amount,
            currency=currency,
            payment_method=payment_method,
            session_id=session_id,
            is_paid=is_paid,
            course_paid=course_paid,
            lesson_paid=lesson_paid_id
        )


class PaymentsRetrieveAPIview(generics.CreateAPIView):
    """Создаем эндпоинт для получения платежа"""
    serializer_class = PaymentsSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        payment_id = Payments.session_id

        stripe.api_key = "sk_test_51OeeJsFwLUbQdeHr078ebwekixI2OAumCmmGC1e0spoY2M9H6eNyuQO0gHSQuC12avF7DqXi4XCgWftsgGGuvn4N00KN2tMZrF"

        try:
            payment_intent = stripe.PaymentIntent.retrieve(payment_id)

            return payment_intent
        except stripe.error.InvalidRequestError:
            raise InvalidRequestError("Платеж не найден")


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


