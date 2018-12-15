from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction

from coffehouse.users.models import BaseUser, Customer, Service


# class RegisterUser(forms.ModelForm):
#     login = forms.CharField(widget=forms.TextInput(), max_length=30, required=True)
#     real_name = forms.CharField(widget=forms.TextInput(), max_length=100, required=True)
#     password = forms.CharField(widget=forms.PasswordInput())
#     email = forms.EmailField(required=True)
#     address = forms.CharField(widget=forms.TextInput(), max_length=100, required=True)
#     country = forms.CharField(widget=forms.TextInput(), max_length=40, required=True)
#
#     class Meta:
#         model = CustomUser
#         fields = ['login', 'real_name', 'password', 'email', 'address', 'country']


class LoginUser(forms.Form):
    login = forms.CharField(widget=forms.TextInput(), max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())


# Not in use ##########################################################################################################
class RegisterNewCustomerForm(UserCreationForm):
    address = forms.CharField(widget=forms.TextInput(), max_length=100, required=True)
    country = forms.CharField(widget=forms.TextInput(), max_length=20, required=True)

    class Meta(UserCreationForm.Meta):
        model = BaseUser
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'country']
        help_texts = {
            'username': ''
        }

        @transaction.atomic
        def save(self):
            user = super().save(commit=False)
            user.save()
            Customer.objects.create(user=user)
            return user


class CustomerChangeForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = UserChangeForm.Meta.fields


class RegisterNewServiceForm(UserCreationForm):
    address = forms.CharField(widget=forms.TextInput(), max_length=100, required=True)
    country = forms.CharField(widget=forms.TextInput(), max_length=20, required=True)
    IBAN = forms.CharField(widget=forms.TextInput(), max_length=100, required=True)

    class Meta:
        model = BaseUser
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'country', 'IBAN']

        @transaction.atomic
        def save(self):
            user = super().save(commit=False)
            user.save()
            Service.objects.create(user=user)
            return user


class UserProfileChange(UserChangeForm):
    address = forms.CharField(widget=forms.TextInput(), max_length=100, required=True)
    country = forms.CharField(widget=forms.TextInput(), max_length=20, required=True)

    class Meta:
        model = BaseUser
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'country']
        help_texts = {
            'username': None
        }
