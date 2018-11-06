from django.db import models

from coffehouse.users.models import CustomUser, Customer


class Food(models.Model):
    name = models.CharField(max_length=50)
    number_in_menu = models.IntegerField(default=-1)
    price = models.DecimalField(max_length=4, max_digits=6, decimal_places=2)
    # quantity = models.IntegerField()
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
    food = models.ForeignKey(Food, related_name='foods', on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, related_name='drinks', on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    note = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "{user_name} ordered something at: {date}".format(user_name=self.user.__str__(),
                                                                 date=self.created_at.__str__())
