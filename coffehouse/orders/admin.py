from django.contrib import admin
from .models import Food, Drink, Order
# Register your models here.

admin.site.register(Food)
admin.site.register(Drink)
admin.site.register(Order)
