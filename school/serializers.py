from rest_framework import serializers

from school.models import Course, Lesson, Payments


class LessonSerializer(serializers.ModelSerializer):  # Generics

    class Meta:
        model = Lesson
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):  # Generics

    class Meta:
        model = Payments
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):  # ViewSet
    # первое задание - выводим все уроки, работает только с count
    count_lessons = serializers.IntegerField(source='lesson.all().count', read_only=True)

    # третье задание - выводим просто уроки судя по всему
    # all_lesson = serializers.SerializerMethodField()  # it works
    all_lesson = LessonSerializer(source='lesson.all', many=True, read_only=True)  # alternative without funcs

    class Meta:
        model = Course
        fields = '__all__'

    # def get_all_lesson(self, instance):
    #     lessons = instance.lesson.all()
    #     return [{'title': lesson.title, 'description': lesson.description}
    #             for lesson in lessons]