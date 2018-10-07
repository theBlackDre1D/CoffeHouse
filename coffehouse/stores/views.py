# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.

# When function parameter has default value this parameter is optional
def detail(request, store_id='1', location=None):

    # Example of accessing query parameters
    # This is example of GET HTTP request. When POST request is the same just
    # GET changes to POST
    hours = request.GET.get('hours', None)
    map = request.GET.get('map', None)

    return render(request, 'stores/detail.html')


def index(request):
    return render(request, 'stores/index.html')
