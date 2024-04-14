from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lesson
from .serializers import LessonSerializer

#Добавление
class LessonList(APIView):
    def post(self, request, format=None):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Получение пар группы
class GroupLessonList(APIView):
    def get(self, request, format=None):
        group = request.data.get('group')
        try:
            lessons = Lesson.objects.filter(group__title=group)
            serializer = LessonSerializer(lessons, many=True)
            return Response(serializer.data)
        except Lesson.DoesNotExist:
            return Response("Уроков для указанной группы не существует", status=status.HTTP_404_NOT_FOUND)

#Получение пар преподавателя
class TeacherLessonList(APIView):
    def get(self, request, format=None):
        teacher = request.data.get('teacher')
        try:
            lessons = Lesson.objects.filter(teacher__full_name=teacher)
            serializer = LessonSerializer(lessons, many=True)
            return Response(serializer.data)
        except Lesson.DoesNotExist:
            return Response("Уроков для указанного преподавателя не существует", status=status.HTTP_404_NOT_FOUND)

