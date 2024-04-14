# Generated by Django 4.2.11 on 2024-04-14 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70, verbose_name='ФИО')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота')], verbose_name='День недели')),
                ('time_start', models.CharField(choices=[('08:30', '08:30'), ('10:00', '10:00'), ('11:40', '11:40'), ('13:30', '13:30'), ('15:00', '15:00'), ('16:30', '16:30')], max_length=5, verbose_name='Время начала')),
                ('time_end', models.CharField(choices=[('08:30', '08:30'), ('10:00', '10:00'), ('11:40', '11:40'), ('13:30', '13:30'), ('15:00', '15:00'), ('16:30', '16:30')], max_length=5, verbose_name='Время окончания')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson.group', verbose_name='Группа')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson.subject', verbose_name='Предмет')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson.teacher', verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Пара',
                'verbose_name_plural': 'Пары',
            },
        ),
    ]