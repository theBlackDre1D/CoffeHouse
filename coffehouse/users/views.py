from django.shortcuts import render

from coffehouse.users.forms import RegisterUser


def show_profile(request):
    return render(request, 'users/user_profile.html')


def login(request):
    return render(request, 'users/login.html')


def register(request):
    if request.method == 'POST':
        new_user = RegisterUser(request.POST)
        if new_user.is_valid():
            new_user.save()

            return render(request, 'users/welcome_new_user.html')
        else:
            return render(request, 'user/register_error.html')
    else:
        form = RegisterUser()

    return render(request, 'users/register.html', {'form': form})
