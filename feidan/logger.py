# -*- coding: utf-8 -*-
# __author__ = ‘du‘
# __created_at__ = '2017/12/12'
import logging
import time
from django.shortcuts import render

logger = logging.getLogger("django")


def api_logger(func):
    """
    接口打日志的装饰器
    :param func:
    :return:
    """
    def inner_func(request):
        try:
            start = time.time()
            result = func(request)
            end = time.time()
            logger.info(
                'Method: {0}, Url: {1}, Body: {2}, COOKIES: {3}, Delay: {4}'.format
                (request.method, request.path, request.body, request.COOKIES, end-start)
            )
        except Exception as e:
            logger.exception(str(e))
            result = render(request, '500.html')
        return result
    return inner_func
