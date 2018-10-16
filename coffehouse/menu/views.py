from django.shortcuts import render
from django.contrib.auth.models import User

from ..orders.models import Order, Food, Drink


def index(request):
    if request.method == 'POST':
        food_name = request.POST['food']
        address = request.POST['address']
        note_from_user = request.POST['note']

        user = User.objects.first()

        order = Order.objects.create(
            user=user,
            food=Food.objects.create(
                name=food_name,
                price=14.25,
                quantity=1),
            processed=False,
            note=note_from_user
        )

        # order.save()

    return render(request, 'menu/index.html')
