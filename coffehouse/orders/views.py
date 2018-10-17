from django.shortcuts import render


def successful_order(request):
    return render(request, 'orders/successful_order.html')
