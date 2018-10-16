from django.contrib.auth.models import User
from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_length=4, max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    note = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_length=4, max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    note = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, related_name='client', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name='foods', on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, related_name='drinks', on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True)
    processed = models.BooleanField()
    note = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "{user_name} ordered something at: {date}".format(user_name=self.user.get_full_name(),
                                                                 date=self.created_at.__str__())
