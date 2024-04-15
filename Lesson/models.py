from django.db import models
from django.db.models import Max
from django.core.exceptions import ValidationError

class Subject(models.Model):
    title = models.CharField(max_length=70, blank=False, verbose_name='Название')
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.title

class Teacher(models.Model):
    full_name = models.CharField(max_length=70, blank=False, verbose_name='ФИО')
    
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return self.full_name
 
class Group(models.Model):
    title = models.CharField(max_length=10, blank=False, verbose_name='Название')
    
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    lesson_number = models.IntegerField(choices=[(1, 'Первая'), (2, 'Вторая'), (3, 'Третья'), (4, 'Четвёртая'), (5, 'Пятая'), (6, 'Шестая')], verbose_name='Номер пары')
    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name='Преподаватель', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница')], verbose_name='День недели')
    
    def clean(self):
        lessons_in_day = Lesson.objects.filter(group=self.group, day_of_week=self.day_of_week)
        num_lessons = lessons_in_day.count()
        print(num_lessons)

        if num_lessons >= 4:
            raise ValidationError("Слишком много пар для этой группы на этот день недели")
        
        lessons_in_day = Lesson.objects.filter(group=self.group, day_of_week=self.day_of_week, lesson_number=self.lesson_number)
        if lessons_in_day.exists():
            raise ValidationError("Пара с таким номером уже существует в этот день недели для данной группы")
        
        max_lesson_number = Lesson.objects.filter(group=self.group, day_of_week=self.day_of_week).aggregate(Max('lesson_number'))['lesson_number__max']
        if max_lesson_number is not None and self.lesson_number != max_lesson_number + 1:
            raise ValidationError("Невозможно создать пару с номером {}. Номер следующей пары должен быть {}.".format(self.lesson_number, max_lesson_number + 1))

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'

    def __str__(self):
        return f"{self.subject} - {self.group} - {self.teacher}"
    
    


