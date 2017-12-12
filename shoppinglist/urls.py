# -*- coding: utf-8 -*-
# __author__ = ‘du‘
# __created_at__ = '2017/12/12'
from django.conf.urls import url

from views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]
