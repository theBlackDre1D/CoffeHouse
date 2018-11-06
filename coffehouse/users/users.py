from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from coffehouse.users.forms import RegisterNewCustomerForm
from coffehouse.users.models import BaseUser, Customer


class RegisterNewCustomerView(CreateView):
    model = Customer
    form_class = RegisterNewCustomerForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        address = form.cleaned_data['address']
        country = form.cleaned_data['country']
        user.is_customer = True
        user.save()
        login(self.request, user)
        Customer.objects.create(user=user, address=address, country=country)
        return redirect('users:welcome')

