from django.db import models

from coffehouse.users.models import Customer, Service


class Food(models.Model):
    name = models.CharField(max_length=50)
    number_in_menu = models.IntegerField(default=-1)
    price = models.DecimalField(max_length=4, max_digits=6, decimal_places=2)
    # quantity = models.IntegerField()
    week_day = models.IntegerField(default=-1)
    img_url = models.CharField(max_length=1000, default=" ")
    description = models.CharField(max_length=1000, default="")
    note = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_length=4, max_digits=6, decimal_places=2)
    # quantity = models.IntegerField()
    description = models.CharField(max_length=1000, default="")
    note = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(Customer, related_name='client', on_delete=models.CASCADE, null=True)
    food = models.ManyToManyField(Food, related_name='foods')
    drink = models.ManyToManyField(Drink, related_name='drinks', default=None)
    created_at = models.DateField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    processed_by = models.ForeignKey(Service, related_name='processed_by', on_delete=models.CASCADE, null=True)
    note = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "{user_name} ordered something at: {date}".format(user_name=self.user.__str__(),
                                                                 date=self.created_at.__str__())


class Chart(models.Model):
    user = models.OneToOneField(Customer, related_name='customer', on_delete=models.CASCADE, null=True)
    food = models.ManyToManyField(Food, related_name='food_in_chart', default=None)
    drink = models.ManyToManyField(Drink, related_name='drinks_in_chart', default=None)
    total_price = models.DecimalField(default=0.0, max_length=4, max_digits=6, decimal_places=2)

    def __str__(self):
        return "{username}' shopping chart".format(username=self.user.__str__())