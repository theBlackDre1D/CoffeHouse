from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#
#
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser
#
#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username']
#
#

# admin.site.register(CustomUser)
from django.contrib.auth.forms import UserChangeForm

from coffehouse.users.models import BaseUser


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = BaseUser


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_owner', 'is_service', 'is_customer')}),
    )


admin.site.register(BaseUser, MyUserAdmin)
