from django.conf.urls import url

from . import views

app_name = 'orders'
urlpatterns = [
    url(r'^unprocessed', views.unprocessed_orders, name='unprocessed')
]
