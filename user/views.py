from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('core:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Login',
        'form': form
    }

    return render(request, 'user/login.html', context)


def register(request):
    context = {
        'title': 'Register'
    }
    return render(request, 'user/register.html', context)


def profile(request):
    context = {
        'title': 'Profile'
    }
    return render(request, 'user/profile.html', context)


def logout(request):
    pass
