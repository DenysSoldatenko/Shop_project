from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.edit import FormView

from order.forms import CreateOrderForm
from order.services import OrderService


class CreateOrderView(LoginRequiredMixin, FormView):
    template_name = 'order/create_order.html'
    form_class = CreateOrderForm
    success_url = 'user:profile'

    def get_initial(self):
        return {
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
        }

    def form_valid(self, form):
        order_service = OrderService(self.request.user, form.cleaned_data)
        try:
            order_service.create_order()
            messages.success(self.request, 'Your order has been placed!')
            return redirect(self.success_url)
        except Exception as e:
            messages.error(self.request, str(e))
            return redirect('cart:order')

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error in the form.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Order Checkout'
        context['order'] = True
        return context
