from django.db import models


class CustomUser(models.Model):
    login = models.CharField(max_length=30)
    real_name = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.login
