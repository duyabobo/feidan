# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class BaseModel(models.Model):
    """基础扩展类"""
    created_at = models.DateTimeField('创建记录时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改日期', auto_now=True)

    @classmethod
    def get_items(cls, page=0, limit=50):
        """
        查询所有记录的最多前50条记录
        :param page:
        :param limit:
        :return:
        """
        return cls.objects.all()[page*limit: (page+1)*limit]

    class Meta:
        abstract = True


class FirstShoppingList(BaseModel):
    """顶级菜单"""
    name = models.CharField('名称', max_length=20, default='')
    serial_number = models.IntegerField('位置序号', default=0)

    class Meta:
        db_table = 't_first_shopping_list'


class SecondShoppingList(BaseModel):
    """二级菜单"""
    first_sl_id = models.IntegerField('所属顶级菜单id', default=1)
    name = models.CharField('名称', max_length=20, default='')
    serial_number = models.IntegerField('位置序号', default=0)

    @classmethod
    def get_items(cls, page=0, limit=50, **kwargs):
        """
        查询某个一级菜单下所有记录的最多前50条记录
        :param page:
        :param limit:
        :param kwargs:
        :return:
        """
        first_sl_id = int(kwargs.get('first_shopping_item_id', 0))
        return cls.objects.filter(first_sl_id=first_sl_id)[page * limit: (page + 1) * limit]
