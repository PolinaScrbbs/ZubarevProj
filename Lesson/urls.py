from django.urls import path
from .views import GroupList, TeacherList, LessonList, GroupLessonList, TeacherLessonList

#Пары
urlpatterns = [
    path('lessons/', LessonList.as_view(), name='lesson-list'),
    path('group_lessons/', GroupLessonList.as_view(), name='group-lesson-list'),
    path('teacher_lessons/', TeacherLessonList.as_view(), name='teacher-lesson-list')
]

#Группы
urlpatterns += [
    path('groups/', GroupList.as_view(), name='group-list'),
]

#Преподаватели
urlpatterns += [
    path('teachers/', TeacherList.as_view(), name='teacher-list'),
]