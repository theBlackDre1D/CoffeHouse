# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse


def index(request):
    redirect_home = HttpResponsePermanentRedirect(reverse('homepage'))

    return render(request, 'about/index.html', {'homepage': redirect_home})


def contact(request):
    return render(request, 'about/contact.html')

