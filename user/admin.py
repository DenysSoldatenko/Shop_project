from django.contrib import admin

from cart.admin import CartTabAdmin
from order.admin import OrderTabularAdmin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email", ]
    search_fields = ["username", "first_name", "last_name", "email", ]

    inlines = [CartTabAdmin, OrderTabularAdmin]
