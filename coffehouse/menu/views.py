from django.shortcuts import render

from coffehouse.users.models import Customer
from ..orders.models import Food, Chart, Drink
from .forms import AddItemToChart


# def index(request):
#     if request.method == 'POST':
#         new_order = NewOrder(request.POST)
#         if new_order.is_valid():
#             user = request.user
#             customer = Customer.objects.get(user=user)
#             menu_number = new_order.cleaned_data.get('menu_number')
#             note = new_order.cleaned_data.get('note')
#             # quantity = new_order.cleaned_data.get('quantity')
#
#             food = Food.objects.get(number_in_menu=menu_number)
#
#             order = new_order.save(commit=False)
#             order.food = food
#             order.user = customer
#             order.note = note
#             order.save()
#
#             return render(request, 'orders/successful_order.html')
#         else:
#             return render(request, 'orders/error_order.html')
#     else:
#         all_food = Food.objects.all()
#         form = NewOrder()
#
#     return render(request, 'menu/menu.html', {'form': form, 'all_food': all_food})

def index(request):
    all_food = Food.objects.all()
    form = AddItemToChart()

    if request.method == 'POST':
        new_order = AddItemToChart(request.POST)
        if new_order.is_valid():
            user = request.user
            customer = Customer.objects.get(user=user)
            chart = Chart.objects.get(user=customer)

            menu_number = new_order.cleaned_data.get('menu_number')
            drink_name = new_order.cleaned_data.get('drink', None)

            food = Food.objects.get(number_in_menu=menu_number)
            if drink_name is not None:
                try:
                    drink = Drink.objects.get(name=drink_name)
                    chart.drinks_in_chart.add(drink)
                except:
                    pass

            chart.food.add(food)

            chart.save()

            return render(request, 'menu/menu.html', {'form': form, 'all_food': all_food})
        else:
            return render(request, 'orders/error_order.html')
    else:
        return render(request, 'menu/menu.html', {'form': form, 'all_food': all_food})
