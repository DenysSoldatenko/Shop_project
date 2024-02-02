from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from user.forms import UserLoginForm, UserRegistrationForm


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
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('core:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Register',
        'form': form
    }

    return render(request, 'user/register.html', context)


def profile(request):
    context = {
        'title': 'Profile'
    }
    return render(request, 'user/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('core:index'))
