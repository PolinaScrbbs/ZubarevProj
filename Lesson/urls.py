from django.urls import path
from .views import LessonList, GroupLessonList, TeacherLessonList

#Пары
urlpatterns = [
    path('lessons/', LessonList.as_view(), name='lesson-list'),
    path('group_lessons/', GroupLessonList.as_view(), name='group-lesson-list'),
    path('teacher_lessons/', TeacherLessonList.as_view(), name='teacher-lesson-list')
]