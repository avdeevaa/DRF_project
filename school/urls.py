from django.urls import path
from rest_framework.routers import DefaultRouter

from school.apps import SchoolConfig
from school.views import CourseViewSet, LessonCreateAPIview, LessonListAPIview, LessonRetrieveAPIview, \
    LessonUpdateAPIview, LessonDestroyAPIview, PaymentsListAPIview

app_name = SchoolConfig.name

router = DefaultRouter()

router.register(r'course', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIview.as_view(), name='create_lesson'),
    path('lesson/', LessonListAPIview.as_view(), name='all_lesson'),
    path('lesson/<int:pk>/', LessonRetrieveAPIview.as_view(), name='get_lesson'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIview.as_view(), name='update_lesson'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIview.as_view(), name='delete_lesson'),

    path('payments/', PaymentsListAPIview.as_view(), name='all_payments'),
] + router.urls
