from django.shortcuts import render
from django.contrib.auth.models import User

from coffehouse.users.models import Customer
from ..orders.models import Food
from .forms import NewOrder


def index(request):
    if request.method == 'POST':
        new_order = NewOrder(request.POST)
        if new_order.is_valid():
            user = request.user
            customer = Customer.objects.get(user=user)
            menu_number = new_order.cleaned_data.get('menu_number')
            note = new_order.cleaned_data.get('note')
            quantity = new_order.cleaned_data.get('quantity')

            food = Food.objects.get(number_in_menu=menu_number)

            order = new_order.save(commit=False)
            order.food = food
            order.user = customer
            order.note = note
            order.save()

            return render(request, 'orders/successful_order.html')
        else:
            return render(request, 'orders/error_order.html')
    else:
        form = NewOrder()

    return render(request, 'menu/index.html', {'form': form})
