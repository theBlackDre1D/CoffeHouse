from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from coffehouse.orders.models import Order, Chart, Food, Drink
from coffehouse.users.models import Service, Customer, BaseUser


def successful_order(request):
    return render(request, 'orders/successful_order.html')


def unsuccessful_order(request):
    return render(request, 'orders/error_order.html')


@login_required
def unprocessed_orders(request):
    if request.user.is_service:
        service = request.user
        orders = Order.objects.filter(processed=False)

        return render(request, 'orders/unprocessed_orders.html', {'orders': orders})

    return redirect('users:login')


def proceed_order(request):
    order_id = request.GET.get('order_id', None)
    success = False
    try:
        order = Order.objects.get(id=order_id)
        service = Service.objects.get(user=request.user)
        order.processed_by = service
        order.processed = True

        order.save()

        success = True
    except:
        success = False

    data = {
        'message': success
    }

    return JsonResponse(data)


@login_required
def cancel_order(request):
    order_id = request.GET.get('order_id', None)
    success = False
    try:
        order = Order.objects.get(id=order_id)
        order.delete()
        success = True
    except:
        success = False

    data = {
        'message': success
    }

    return JsonResponse(data)


@login_required
def show_chart(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    chart = Chart.objects.get(user=customer)

    food = chart.food.all()
    drinks = chart.drink.all()

    if request.GET.get('order'):
        new_order = Order()
        new_order.user = customer
        new_order.save()

        food_list = list(chart.food.all())
        for food in food_list:
            db_food = Food.objects.get(name=food.name)
            new_order.food.add(db_food)

        drink_list = list(chart.drink.all())
        for drink in drink_list:
            db_drink = Drink.objects.get(name=drink.name)
            new_order.drink.add(db_drink)

        new_order.total_price = chart.total_price
        new_order.save()

        chart.food.clear()
        chart.drink.clear()
        chart.total_price = 0.0
        chart.save()

        return render(request, 'orders/successful_order.html')

    return render(request, 'orders/show_chart.html', {'food': food, 'drinks': drinks, 'total_price': chart.total_price})


@login_required(login_url='/users/login')
def orders_history(request):
    user = request.user
    customer = Customer.objects.get(user=user)

    customer_orders = Order.objects.filter(user=customer)

    return render(request, 'orders/orders_history.html', {'orders': customer_orders})
