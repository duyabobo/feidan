# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from feidan.logger import api_logger
from utils.first_shopping_list import get_first_shopping_list_context

# Create your views here.


@api_logger
def index(request):
    """首页，展示顶级品类菜单"""
    context = get_first_shopping_list_context()
    return render(
        request,
        'index.html',
        context=context
    )
