# -*- coding: utf-8 -*-
# __author__ = ‘du‘
# __created_at__ = '2017/12/12'
import logging
from django.shortcuts import render

logger = logging.getLogger("django")  # 为loggers中定义的名称


def api_logger(func):
    """
    接口打日志的装饰器
    :param func:
    :return:
    """
    def inner_func(request):
        try:
            result = func(request)
        except Exception as e:
            logger.exception(str(e))
            result = render(request, '500.html')
        return result
    return inner_func
