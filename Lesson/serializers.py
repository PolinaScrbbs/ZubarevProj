from rest_framework import serializers
from .models import Lesson, Subject, Teacher, Group

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'title')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'full_name')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title')

class LessonSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    teacher = TeacherSerializer()
    group = GroupSerializer()

    class Meta:
        model = Lesson
        fields = ('id', 'subject', 'teacher', 'group', 'day_of_week', 'time_start', 'time_end')