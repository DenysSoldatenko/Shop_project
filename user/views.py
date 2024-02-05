from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from user.forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'Successfully logged in!')
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
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
            messages.success(request, 'Registration successful! You are now logged in')
            return HttpResponseRedirect(reverse('core:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Register',
        'form': form
    }

    return render(request, 'user/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully')
            return HttpResponseRedirect(reverse('user:profile'))
        else:
            messages.error(request, 'Please correct the errors below')
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Profile',
        'form': form
    }

    return render(request, 'user/profile.html', context)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect(reverse('core:index'))
