from django.contrib.auth.models import AbstractUser
from django.db import models


# class CustomUser(models.Model):
#     # class CustomUser(AbstractUser):
#     login = models.CharField(max_length=30)
#     real_name = models.CharField(max_length=100)
#     password = models.CharField(max_length=200)
#     email = models.EmailField()
#     address = models.CharField(max_length=100, default=" ")
#     country = models.CharField(max_length=40, default=" ")
#
#     def __str__(self):
#         return self.login


class BaseUser(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_service = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Customer(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=40, default=" ")

    def __str__(self):
        return self.user.username


class Service(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, primary_key=True)
    start_date = models.DateField(auto_now_add=True)
