from django.shortcuts import render, redirect

from coffehouse.users.forms import RegisterUser, RegisterNewCustomerForm, LoginUser
from coffehouse.users.models import Customer, CustomUser


def show_profile(request):
    return render(request, 'users/user_profile.html')


def test_register(request):
    if request.method == 'POST':
        new_customer = RegisterNewCustomerForm(request.POST)
        if new_customer.is_valid():
            new_customer.save(commit=False)

            return render(request, 'users/welcome_new_user.html')
        else:
            reasons = new_customer.error_messages.items()
            return render(request, 'users/register_error.html', {'reasons': reasons})
    else:
        form = RegisterNewCustomerForm()

    return render(request, 'users/test_register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        visitor = LoginUser(request.POST)
        if visitor.is_valid():
            try:
                user = CustomUser.objects.get(login=visitor.cleaned_data['login'])
                if user.password != visitor.cleaned_data['password']:
                    raise ValueError('Wrong password!')
            except ValueError as e:
                error = e.args
                return render(request, 'users/register_error.html', {'reasons': error})
        # else:
        #     dsfs
    else:
        form = LoginUser
    return render(request, 'users/login.html', {'form': form})


def welcome(request):
    return render(request, 'users/welcome_new_user.html')


def register(request):
    if request.method == 'POST':
        new_user = RegisterUser(request.POST)
        if new_user.is_valid():
            new_user.save()

            return render(request, 'users/welcome_new_user.html')
        else:
            return render(request, 'users/register_error.html')
    else:
        form = RegisterUser()

    return render(request, 'users/register.html', {'form': form})
