import re

from django import forms
from django.core.exceptions import ValidationError


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
        ],
    )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
        ],
    )

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        cleaned_data = re.sub(r'\D', '', data)

        if len(cleaned_data) != 10:
            raise ValidationError("The phone number should contain exactly 10 digits.")

        if not cleaned_data.isdigit():
            raise ValidationError("The phone number should contain only digits.")

        return data
