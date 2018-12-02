from django.conf.urls import url

from . import views

app_name = 'orders'
urlpatterns = [
    url(r'^unprocessed', views.unprocessed_orders, name='unprocessed'),
    url(r'^proceed', views.proceed_order, name='proceed_order'),
    url(r'^show_chart', views.show_chart, name='show_chart'),
]
