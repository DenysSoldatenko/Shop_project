from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from cart.models import Cart
from order.forms import CreateOrderForm
from order.models import Order, OrderItem


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if not cart_items.exists():
                        messages.error(request, 'Your cart is empty.')
                        return redirect('cart:order')

                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data['phone_number'],
                        requires_delivery=form.cleaned_data['requires_delivery'],
                        delivery_address=form.cleaned_data['delivery_address'],
                        payment_on_get=form.cleaned_data['payment_on_get'],
                    )

                    for cart_item in cart_items:
                        product = cart_item.product
                        if product.quantity < cart_item.quantity:
                            raise ValidationError(
                                f'Insufficient stock for product {product.name}. Available stock: {product.quantity}.'
                            )

                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=product.name,
                            price=product.get_sale_price(),
                            quantity=cart_item.quantity,
                        )

                        product.quantity -= cart_item.quantity
                        product.save()

                    cart_items.delete()
                    messages.success(request, 'Your order has been placed!')
                    return redirect('user:profile')

            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('cart:order')

    else:
        form = CreateOrderForm(initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        })

    return render(request, 'order/create_order.html', {'form': form, 'title': 'Order Checkout', 'order': True})
