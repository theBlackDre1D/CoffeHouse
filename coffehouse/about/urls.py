from django.conf.urls import url
from . import views

app_name = 'about'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact')
]
