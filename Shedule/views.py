from django.shortcuts import render
import requests

def index(request):
    token = request.session.get('token')
    if token:
        api_url = f'http://127.0.0.1:8000/auth/signup/?token={token}'
        response = requests.get(api_url)

        if response.status_code == 200:
            user = response.json()['Пользователь']
        else:
            print("Ошибка:", response.status_code)
    else:
        user = None

    # Выполняем GET-запрос к вашему API для получения списка преподавателей
    api_url = 'http://127.0.0.1:8000/api/groups/'
    response = requests.get(api_url)

    if response.status_code == 200:
        # Если запрос успешен, получаем данные о преподавателях из ответа API
        groups = response.json()

        # Передаем данные о преподавателях в контекст представления
        context = {
            'user': user,
            'title': 'Рассписание',
            'groups': groups
        }
        return render(request, 'index.html', context)
    else:
        # Если запрос не удался, возвращаем пустой список преподавателей
        groups = []
        context = {
            'user': user,
            'title': 'Рассписание',
            'groups': groups
        }
        return render(request, 'index.html', context)
    
def schedule(request, group):
    token = request.session.get('token')
    if token:
        api_url = f'http://127.0.0.1:8000/auth/signup/?token={token}'
        response = requests.get(api_url)

        if response.status_code == 200:
            user = response.json()['Пользователь']
        else:
            print("Ошибка:", response.status_code)
    else:
        user = None

    # Выполняем GET-запрос к вашему API для получения списка уроков
    api_url = 'http://127.0.0.1:8000/api/group_lessons/'
    data  = {"group": group}
    response = requests.get(api_url, data=data)
    
    if response.status_code == 200:
        # Если запрос успешен, получаем данные о уроках из ответа API
        lessons_data = response.json()

        # Создаем словарь для хранения уроков по дням недели
        schedule_dict = {
            'Понедельник': [],
            'Вторник': [],
            'Среда': [],
            'Четверг': [],
            'Пятница': [],
        }

        # Заполняем словарь уроками из полученных данных
        for lesson in lessons_data:
            day_of_week = lesson['day_of_week']
            lesson_info = {
                'lesson_number': int(lesson['lesson_number']),
                'subject': lesson['subject']['title'],
                'teacher': lesson['teacher']['full_name'],
                'group': lesson['group']['title'],
            }
            # Добавляем урок в соответствующий день недели
            if day_of_week == 1:
                schedule_dict['Понедельник'].append(lesson_info)
            elif day_of_week == 2:
                schedule_dict['Вторник'].append(lesson_info)
            elif day_of_week == 3:
                schedule_dict['Среда'].append(lesson_info)
            elif day_of_week == 4:
                schedule_dict['Четверг'].append(lesson_info)
            elif day_of_week == 5:
                schedule_dict['Пятница'].append(lesson_info)

        # Передаем данные о расписании в контекст представления

        context = {
            'user': user,
            'title': 'Расписание',
            'schedules': schedule_dict,
            'lesson_times' : {
                1: ("8:30", "09:50"),
                2: ("10:00", "11:20"),
                3: ("11:40", "13:00"),
                4: ("13:30", "14:50"),
                5: ("15:00", "16:20"),
                6: ("16:30", "17:50")
            }
        }
        return render(request, 'schedule.html', context)
    else:
        # Если запрос не удался, возвращаем пустой словарь расписания
        schedule_dict = {
            'Понедельник': [],
            'Вторник': [],
            'Среда': [],
            'Четверг': [],
            'Пятница': [],
        }
        context = {
            'user': user,
            'title': 'Расписание',
            'schedules': schedule_dict
        }
        return render(request, 'shedule.html', context)


