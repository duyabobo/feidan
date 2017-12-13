# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from feidan.logger import api_logger
from utils.first_shopping_list import get_first_shopping_list_context

# Create your views here.


@api_logger
def index(request):
    """首页，展示顶级品类菜单"""
    context = get_first_shopping_list_context()  # todo 放redis
    return render(
        request,
        'index.html',
        context=context
    )


@api_logger
def second_index(request, name):
    """
    展示二级品类菜单
    :param request:
    :param name: 一级品类名称，中文
    :return:
    """
    context = {'name': name}
    return render(
        request,
        'second_index.html',
        context=context
    )
