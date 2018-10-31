from django.shortcuts import render

from coffehouse.users.forms import RegisterUser


def show_profile(request):
    return render(request, 'users/user_profile.html')


def test_register(request):
    return render(request, '')

def login(request):
    return render(request, 'users/login.html')


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
