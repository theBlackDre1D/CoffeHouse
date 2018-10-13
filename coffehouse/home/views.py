from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse


def home_page(request):
    # redirect_stores = HttpResponsePermanentRedirect(reverse('stores'))
    #
    # render_in_template = {'stores': redirect_stores}
    return render(request, 'homepage.html')
