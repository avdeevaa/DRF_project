from rest_framework import serializers

from school.models import Course, Lesson, Payments, Subscription
from school.validators import URLValidator


class LessonSerializer(serializers.ModelSerializer):  # Generics

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [URLValidator(field='url')]


class PaymentsSerializer(serializers.ModelSerializer):  # Generics

    class Meta:
        model = Payments
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):  # Generics

    class Meta:
        model = Subscription
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Subscription.objects.all(),
                fields=['user', 'course'],
                message='User already subscribed to this course.'
            )
        ]


class CourseSerializer(serializers.ModelSerializer):  # ViewSet
    # первое задание - выводим все уроки, работает только с count
    count_lessons = serializers.IntegerField(source='lesson.all().count', read_only=True)

    # третье задание - выводим просто уроки судя по всему
    # all_lesson = serializers.SerializerMethodField()  # it works
    all_lesson = LessonSerializer(source='lesson.all', many=True, read_only=True)  # alternative without funcs

    new_description = serializers.CharField(source='description')

    class Meta:
        model = Course
        fields = '__all__'

    # def get_all_lesson(self, instance):
    #     lessons = instance.lesson.all()
    #     return [{'title': lesson.title, 'description': lesson.description}
    #             for lesson in lessons]
