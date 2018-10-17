from django.shortcuts import render
from django.contrib.auth.models import User

from ..orders.models import Order, Food, Drink
from .forms import NewOrder


def index(request):
    if request.method == 'POST':
        # food_name = request.POST['food']
        # address = request.POST['address']
        # note_from_user = request.POST['note']
        #
        # user = User.objects.first()
        #
        # order = Order.objects.create(
        #     user=user,
        #     food=Food.objects.create(
        #         name=food_name,
        #         price=14.25,
        #         quantity=1),
        #     processed=False,
        #     note=note_from_user
        # )
        #
        # # order.save()
        new_order = NewOrder(request.POST)
        if new_order.is_valid():
            user = User.objects.first()
            food_name = new_order.cleaned_data.get('food_name')
            note = new_order.cleaned_data.get('note')
            quantity = new_order.cleaned_data.get('quantity')

            order = new_order.save(commit=False)
            order.food = Food.objects.create(
                name=food_name,
                price=14.69,
                quantity=quantity
            )
            order.user = user
            order.note = note
            order.save()

            return render(request, 'orders/successful_order.html')
        else:
            return render(request, 'orders/error_order.html')
    else:
        form = NewOrder()

    return render(request, 'menu/index.html', {'form': form})
