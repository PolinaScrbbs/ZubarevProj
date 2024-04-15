from django.shortcuts import render, redirect
from .forms import LoginForm
from rest_framework import status
import requests
from django.http import HttpResponse

def login(request):
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next')

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        api_url = 'http://127.0.0.1:8000/auth/login/'
        response = requests.post(api_url, data={'email': email, 'password': password})

        if response.status_code == 200:
            token = response.json().get('token')
            request.session['token'] = token
            
            # Если есть параметр next, выполняем перенаправление на него
            if next_url:
                return redirect(next_url)

            # Если параметра next нет, можно выполнить перенаправление на главную страницу
            # return redirect('index')

            return HttpResponse({'token': token}, status=status.HTTP_200_OK)
        else:
            return HttpResponse({'error': 'Failed to get token'}, status=status.HTTP_400_BAD_REQUEST)

    return render(request, 'login.html', {'form': form})



