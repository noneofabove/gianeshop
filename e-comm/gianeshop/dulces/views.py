# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
# Create your views here.


def dash(request):
    return render(request, 'index.html')
