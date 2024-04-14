from django.contrib import admin
from .models import Subject, Teacher, Group, Lesson

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'group', 'day_of_week', 'time_start', 'time_end')
