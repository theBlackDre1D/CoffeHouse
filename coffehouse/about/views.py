# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse

from coffehouse.users.key.key import Key


def index(request):
    redirect_home = HttpResponsePermanentRedirect(reverse('homepage'))

    return render(request, 'about/index.html', {'homepage': redirect_home})


def contact(request):
    return render(request, 'about/contact.html')


def find_us(request):
    key = Key().get_key()
    return render(request, 'about/find_us.html', {'key': key})

