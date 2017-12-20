# -*- coding: utf-8 -*-
# __author__ = ‘du‘
# __created_at__ = '2017/12/12'
from django.conf.urls import url

from views import index, second_index, third_index, second_tag_index

urlpatterns = [
    url(r'^first$', index, name='first_shopping_list'),
    url(r'^second/(?P<first_shopping_item_id>\w+)/$', second_index, name='second_shopping_list'),
    url(r'^third/(?P<second_shopping_item_id>\w+)/$', third_index, name='third_shopping_list'),
    url(r'^second_tag/(?P<second_shopping_item_id>\w+)/$', second_tag_index, name='second_shopping_tag_list')
]
