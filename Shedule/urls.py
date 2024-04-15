from django.urls import path
from .views import index, schedule

urlpatterns = [
    path('index', index, name='index'),
    path('shedule/<str:group>', schedule, name='shedule'),
]