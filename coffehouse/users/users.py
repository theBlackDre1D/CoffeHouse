from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from coffehouse.users.forms import RegisterNewCustomerForm, RegisterNewServiceForm, UserProfileChange
from coffehouse.users.models import BaseUser, Customer, Service


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

        return redirect('home:homepage')


class RegisterNewServiceView(CreateView):
    model = Service
    form_class = RegisterNewServiceForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'service'

        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        address = form.cleaned_data['address']
        country = form.cleaned_data['country']
        IBAN = form.cleaned_data['IBAN']
        user.is_service = True
        user.save()
        # login(self.request, user) don't want to login service after creation account
        Service.objects.create(user=user, address=address, country=country, IBAN=IBAN)

        return redirect('home:homepage')


class CustomerProfileChangeView(CreateView):
    model = Customer
    form_class = UserProfileChange
    template_name = 'users/change_profile.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'

        return super().get_context_data(**kwargs)

    def form_invalid(self, form):
        user = BaseUser.objects.get(username=self.request.user.username)
        current_customer = Customer.objects.get(user=user)
        # user = form.save()
        address = form.cleaned_data['address']
        country = form.cleaned_data['country']

        if current_customer.address != address and address is not None and address is not " ":
            current_customer.address = address

        if current_customer.country is not country and country is not None and country is not " ":
            current_customer.country = country

        current_customer.save()

        return redirect('users:profile')
