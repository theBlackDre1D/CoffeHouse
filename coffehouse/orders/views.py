from django.shortcuts import render

from coffehouse.orders.models import Order


def successful_order(request):
    return render(request, 'orders/successful_order.html')


def unsuccessful_order(request):
    return render(request, 'orders/error_order.html')


def unprocessed_orders(request):
    if request.user.is_authentificated() and request.user.is_service:
        service = request.user
        orders = Order.objects.get(processed=False)

    return render(request)
