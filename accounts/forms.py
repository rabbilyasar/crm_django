from django import forms
from accounts.models import *


class OrderForm(forms.ModelForm):
    """Order form."""

    class Meta:
        """Meta definition for Orderform."""

        model = Order
        fields = ('__all__')
