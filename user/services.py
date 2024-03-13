from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from cart.models import Cart


class UserLoginService:
    def __init__(self, request, form):
        self.request = request
        self.form = form

    def login(self):
        session_key = self.request.session.session_key
        user = self.form.get_user()

        if user:
            auth.login(self.request, user)
            if session_key:
                self._handle_cart_migration(session_key, user)

            messages.success(self.request, f"{user.username}, You have logged in successfully!")
            return HttpResponseRedirect(self.get_success_url())

    def _handle_cart_migration(self, session_key, user):
        forgot_carts = Cart.objects.filter(user=user)
        if forgot_carts.exists():
            forgot_carts.delete()
        Cart.objects.filter(session_key=session_key).update(user=user)

    def get_success_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('user:logout'):
            return redirect_page
        return reverse_lazy('core:index')


class UserRegistrationService:
    def __init__(self, request, form):
        self.request = request
        self.form = form

    def register(self):
        session_key = self.request.session.session_key
        user = self.form.instance

        if user:
            self.form.save()
            auth.login(self.request, user)

        if session_key:
            Cart.objects.filter(session_key=session_key).update(user=user)

        messages.success(self.request, f"{user.username}, You have successfully registered and logged in!")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('user:profile')
