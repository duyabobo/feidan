# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from feidan.logger import api_logger

# Create your views here.


@api_logger
def index(request):
    return render(
        request,
        'index.html'
    )
