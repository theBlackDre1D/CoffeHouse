from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from coffehouse.orders.models import Order, Chart
from coffehouse.users.models import Service, Customer


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
def show_chart(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    chart = Chart.objects.get(user=customer)

    food = chart.food.all()
    drinks = chart.drink.all()

    return render(request, 'orders/show_chart.html', {'food': food, 'drinks': drinks, 'total_price': chart.total_price})
