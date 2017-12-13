# -*- coding: utf-8 -*-
# __author__ = ‘du‘
# __created_at__ = '2017/12/12'
from django.conf.urls import url

from views import index, second_index

urlpatterns = [
    url(r'^first$', index, name='first_shopping_list'),
    url(r'^second/(?P<name>\w+)/$', second_index, name='second_shopping_list'),
]
