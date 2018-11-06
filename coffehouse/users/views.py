from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from coffehouse.users.forms import RegisterUser, RegisterNewCustomerForm, LoginUser


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


def login_user(request):
    if request.method == 'POST':
        visitor = LoginUser(request.POST)
        if visitor.is_valid():
            username = visitor.cleaned_data['login']
            password = visitor.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return render(request, 'homepage.html')
            else:
                error = ValueError("Bad credentials!")
                return render(request, 'some_error.html', {'reasons': error.args})

    form = LoginUser
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)

    return render(request, 'homepage.html')


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
