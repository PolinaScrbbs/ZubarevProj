from django.db import models
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
    # Начало пар
    START_TIME_CHOICES = (
        ('8:30', '8:30'),
        ('10:00', '10:00'),
        ('11:40', '11:40'),
        ('13:30', '13:30'),
        ('15:00', '15:00'),
        ('16:30', '16:30')
    )

    # Конец пар
    END_TIME_CHOICES = (
        ('9:50', '9:50'),
        ('11:20', '11:20'),
        ('13:00', '13:00'),
        ('14:50', '14:50'),
        ('16:20', '16:20'),
        ('17:50', '17:50')
    )

    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name='Преподаватель', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота')], verbose_name='День недели')
    time_start = models.CharField(max_length=5, choices=START_TIME_CHOICES, verbose_name='Время начала')
    time_end = models.CharField(max_length=5, choices=END_TIME_CHOICES, verbose_name='Время окончания')
    
    def clean(self):
        lessons_in_day = Lesson.objects.filter(group=self.group, day_of_week=self.day_of_week)

        num_lessons = lessons_in_day.count()

        if num_lessons > 6:
            raise ValidationError("Слишком много пар для этой группы на этот день недели")
        
        empty_lessons = lessons_in_day.filter(subject=None)
        num_empty_lessons = empty_lessons.count()
        if num_empty_lessons < 2:
            raise ValidationError("Должно быть как минимум две пустые пары для этой группы на этот день недели")
        
        if self.time_start >= self.time_end:
            raise ValidationError("Время начала должно быть раньше времени окончания")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'

    def __str__(self):
        return f"{self.subject} - {self.group} - {self.teacher}"
    
    


