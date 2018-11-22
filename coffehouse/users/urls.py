from django.conf.urls import url

from . import views
from . import users

app_name = 'users'
urlpatterns = [
    url(r'^$', views.show_profile, name='index'),
    # url(r'^register', views.register, name='register'),
    url(r'^login', views.login_user, name='login'),
    url(r'^logout', views.logout_user, name='logout'),
    url(r'^test/', users.RegisterNewCustomerView.as_view(), name='test_register'),
    url(r'^service-register/', users.RegisterNewServiceView.as_view(), name='register_service'),
    url(r'^welcome', views.welcome, name='welcome'),
    url(r'^profile', views.show_profile, name='show_profile'),
    url(r'^change-profile', users.CustomerProfileChangeView.as_view(), name='change_profile'),
    # url(r'^welcome', views.welcome, name='welcome')
]
