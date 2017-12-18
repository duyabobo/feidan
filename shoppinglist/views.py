# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from feidan.logger import api_logger
from db_utils.first_shopping_list import get_first_shopping_list_context
from db_utils.second_shopping_list import get_second_shopping_list_context

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
def second_index(request, first_shopping_item_id):
    """
    展示二级品类菜单
    :param request:
    :param first_shopping_item_id: 一级品类序列号
    :return:
    """
    context = get_second_shopping_list_context(first_shopping_item_id)
    return render(
        request,
        'second_index.html',
        context=context
    )
