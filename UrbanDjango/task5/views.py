from itertools import repeat

from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister

# Create your views here.

users = {'vasya':('dadadada',20), 'petya':('dadadada',19), 'masha':('netnetnet',19)}
info = {}
form = None

def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print(f'username: {username}')
        print(f'password: {password}')
        print(f'age: {age}')

        error = True

        info['username'] = username
        info['password'] = password
        info['repeat_password'] = repeat_password
        info['age'] = age

        info['error'] = ''

        if username in [u_.lower() for u_ in users.keys()]:
            info['error'] += 'Имя пользователя занято. Попробуйте другое. * '
        if repeat_password != password:
            info['error'] += 'Пароли не совпадают. Попробуйте ещё раз.'
        if not info['error']:
            users[username] = (password, age)
            return HttpResponse(content=f'Вы успешно зарегистрировались! Приветствуем, {username}!')

        return render(request,'registration_page.html',context = info)

    return render(request, 'registration_page.html')

def sign_up_by_django(request):
    global form

    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            info = {'form': form, 'error': ''}

            if username in [u_.lower() for u_ in users.keys()]:
                info['error'] += 'Имя пользователя занято. Попробуйте другое. * '
            if repeat_password != password:
                info['error'] += 'Пароли не совпадают. Попробуйте ещё раз.'
            if not info['error']:
                users[username] = (password, age)
                return HttpResponse(content=f'Вы успешно зарегистрировались! Приветствуем, {username}!')
    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'registration_page_dj.html', context=info)
