from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from cart.models import Cart
from order.models import Order, OrderItem
from user.forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, 'Successfully logged in!')
                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)
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
            session_key = request.session.session_key
            user = form.instance
            auth.login(request, user)
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
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


    orders = Order.objects.filter(user=request.user).prefetch_related(
        Prefetch(
            "orderitem_set",
            queryset=OrderItem.objects.select_related("product"),
        )
    ).order_by("-id")

    context = {
        'title': 'Profile',
        'form': form,
        'orders': orders,
    }

    return render(request, 'user/profile.html', context)


class UserCartView(TemplateView):
    template_name = 'user/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cart'
        return context


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect(reverse('core:index'))
