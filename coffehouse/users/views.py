from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from coffehouse.users.forms import RegisterNewCustomerForm, LoginUser
from coffehouse.users.models import BaseUser


def show_profile(request):
    return render(request, 'users/profile.html')


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


def creation_service_success(request):
    return render(request, 'users/welcome_new_user.html')


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': BaseUser.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


# def register(request):
#     if request.method == 'POST':
#         new_user = RegisterUser(request.POST)
#         if new_user.is_valid():
#             new_user.save()
#
#             return render(request, 'users/welcome_new_user.html')
#         else:
#             return render(request, 'users/register_error.html')
#     else:
#         form = RegisterUser()
#
#     return render(request, 'users/register.html', {'form': form})
