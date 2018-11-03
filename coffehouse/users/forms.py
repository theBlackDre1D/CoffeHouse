from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from coffehouse.users.models import CustomUser, BaseUser, Customer


class RegisterUser(forms.ModelForm):
    login = forms.CharField(widget=forms.TextInput(), max_length=30, required=True)
    real_name = forms.CharField(widget=forms.TextInput(), max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)
    address = forms.CharField(widget=forms.TextInput(), max_length=100, required=True)
    country = forms.CharField(widget=forms.TextInput(), max_length=40, required=True)

    class Meta:
        model = CustomUser
        fields = ['login', 'real_name', 'password', 'email', 'address', 'country']


class LoginUser(forms.Form):
    login = forms.CharField(widget=forms.TextInput(), max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())


# Not in use
class RegisterNewCustomerForm(UserCreationForm):
    address = forms.CharField(widget=forms.TextInput(), max_length=100, required=True)
    country = forms.CharField(widget=forms.TextInput(), max_length=20, required=True)

    class Meta(UserCreationForm.Meta):
        model = BaseUser

        @transaction.atomic
        def save(self):
            user = super().save(commit=False)
            user.is_customer = True
            user.save()

            customer = Customer.objects.create(user=user)
            return user
