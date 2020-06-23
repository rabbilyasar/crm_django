from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("__all__")
        exclude = ['user']


class OrderForm(forms.ModelForm):
    """Order form."""
    class Meta:
        """Meta definition for Orderform."""
        model = Order
        fields = ('__all__')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        # for key, field in self.fields.items():
        #     if isinstance(field.widget, forms.TextInput) or \
        #         isinstance(field.widget, forms.Textarea) or \
        #         isinstance(field.widget, forms.DateInput) or \
        #         isinstance(field.widget, forms.DateTimeInput) or \
        #         isinstance(field.widget, forms.TimeInput):
        #             field.widget.attrs.update({'placeholder': field.label})
