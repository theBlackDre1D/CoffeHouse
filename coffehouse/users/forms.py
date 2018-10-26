from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from coffehouse.users.models import CustomUser


class RegisterUser(forms.ModelForm):
    login = forms.CharField(widget=forms.TextInput(), max_length=30, required=True)
    real_name = forms.CharField(widget=forms.TextInput(), max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['login', 'real_name', 'password', 'email']

#
# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = ('username', 'email')
#
#
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')