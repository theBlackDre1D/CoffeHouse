from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from coffehouse.orders.models import Order


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
