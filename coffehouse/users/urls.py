from django.conf.urls import url
from . import views
from . import users

app_name = 'menu'
urlpatterns = [
    url(r'^$', views.show_profile, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login, name='login'),
    # url(r'^test/', users.RegisterNewCustomerView.as_view(), name='test_register')
    url(r'^test/', views.test_register, name='test_register')

    # url(r'^welcome', views.welcome, name='welcome')
]
