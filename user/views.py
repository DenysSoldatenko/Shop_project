from django.shortcuts import render

def login(request):
    context = {
        'title': 'Login'
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
