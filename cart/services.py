from cart.models import Cart


class CartAddService:
    def __init__(self, request, product):
        self.request = request
        self.product = product

    def add_product_to_cart(self):
        cart = self.get_cart_for_product()

        if cart:
            cart.quantity += 1
            cart.save()
        else:
            self.create_new_cart_item()

    def get_cart_for_product(self):
        return Cart.objects.filter(
            product=self.product,
            user=self.request.user if self.request.user.is_authenticated else None,
            session_key=self.request.session.session_key if not self.request.user.is_authenticated else None
        ).first()

    def create_new_cart_item(self):
        Cart.objects.create(
            user=self.request.user if self.request.user.is_authenticated else None,
            session_key=self.request.session.session_key if not self.request.user.is_authenticated else None,
            product=self.product,
            quantity=1
        )


class CartChangeService:
    def __init__(self, request, cart_id, new_quantity):
        self.request = request
        self.cart_id = cart_id
        self.new_quantity = new_quantity

    def update_cart_item(self):
        cart = Cart.objects.get(id=self.cart_id)
        cart.quantity = self.new_quantity
        cart.save()
        return cart


class CartRemoveService:
    def __init__(self, request, cart_id):
        self.request = request
        self.cart_id = cart_id

    def remove_cart_item(self):
        cart = Cart.objects.get(id=self.cart_id)
        product = cart.product
        quantity = cart.quantity
        cart.delete()
        return product, quantity
