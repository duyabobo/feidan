# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from feidan.settings import ONE_PAGE_LIMIT


# Create your models here.


class BaseModel(models.Model):
    """基础扩展类"""
    serial_number = models.FloatField('位置序号', default=0)
    created_at = models.DateTimeField('创建记录时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改日期', auto_now=True)

    @classmethod
    def get_total(cls, father_id):
        """
        查询孩子菜单的总数
        :param father_id:
        :return:
        """
        return cls.objects.filter(father_id=father_id).count()

    @classmethod
    def get_items(cls, page=0, limit=ONE_PAGE_LIMIT):
        """
        查询所有记录的最多前50条记录
        :param page:
        :param limit:
        :return:
        """
        return cls.objects.all().order_by('serial_number')[page*limit: (page+1)*limit]

    @classmethod
    def get_items_by_father_id(cls, father_id, page=0, limit=ONE_PAGE_LIMIT):
        """
        查询某级菜单下子菜单记录的最多前50条记录
        :param father_id:
        :param page:
        :param limit:
        :return:
        """
        if father_id != 'undefined':
            return cls.objects.filter(father_id=father_id).order_by('serial_number')[page * limit: (page + 1) * limit]
        else:
            return []

    class Meta:
        abstract = True


class FirstShoppingList(BaseModel):
    """顶级菜单"""
    name = models.CharField('名称', max_length=20, default='')

    class Meta:
        db_table = 't_first_shopping_list'


class SecondShoppingList(BaseModel):
    """二级菜单"""
    father_id = models.IntegerField('所属顶级菜单id', default=1)
    name = models.CharField('名称', max_length=20, default='')


class ThirdShoppingList(BaseModel):
    """三级菜单，即最终的具体商品品类"""
    father_id = models.IntegerField('所属二级菜单id', default=1)
    name = models.CharField('名称', max_length=50, default='')
    status = models.IntegerField('状态', default=0)  # 0：上线，1：在售，2：售罄，3：下架


class SecondShoppingTagList(BaseModel):
    """二级菜单的tag"""
    father_id = models.IntegerField('所属二级菜单id', default=1)
    name = models.CharField('名称', max_length=50, default='')
