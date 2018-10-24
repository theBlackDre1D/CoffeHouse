from django.conf.urls import url
from . import views

app_name = 'menu'
urlpatterns = [
    url(r'^$', views.show_profile, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login, name='login')
]
