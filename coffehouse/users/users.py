from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from coffehouse.users.forms import RegisterNewCustomerForm
from coffehouse.users.models import BaseUser


class RegisterNewCustomerView(CreateView):
    model = BaseUser
    form_class = RegisterNewCustomerForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users:welcome')


