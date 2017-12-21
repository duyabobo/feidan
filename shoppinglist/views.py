# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from feidan.logger import api_logger
from db_utils.first_shopping_list import get_first_shopping_list_context
from db_utils.second_shopping_list import get_second_shopping_list_context
from db_utils.third_shopping_list import get_third_shopping_list_context
from db_utils.third_shopping_list import get_third_shopping_list_total
from db_utils.second_shoppint_tag_list import get_second_shopping_tag_list_context
from feidan.settings import ONE_PAGE_LIMIT

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


@api_logger
def second_tag_index(request, second_shopping_item_id):
    """
    展示二级品类的 tag
    :param request:
    :param second_shopping_item_id:
    :return:
    """
    context = get_second_shopping_tag_list_context(second_shopping_item_id)
    return render(
        request,
        'second_tag.html',
        context=context
    )


@api_logger
def third_index(request, second_shopping_item_id):
    """
    展示三级品类菜单
    :param request:
    :param second_shopping_item_id:
    :return:
    """
    page = int(request.GET.get('page', 0))
    context = get_third_shopping_list_context(second_shopping_item_id, page=page)  # todo 加上 tag 检索
    return render(
        request,
        'third_index.html',
        context=context
    )


@api_logger
def get_pager(request, second_shopping_item_id):
    """
    获取分页数据
    :param request:
    :param second_shopping_item_id:
    :return:
    """
    total = get_third_shopping_list_total(second_shopping_item_id)  # todo 加上 tag 检索
    return render(request, 'pager_info.html', context={
        'total': total,
        'total_page': int(total/ONE_PAGE_LIMIT) + 1 if total % ONE_PAGE_LIMIT else int(total/ONE_PAGE_LIMIT)
    })
