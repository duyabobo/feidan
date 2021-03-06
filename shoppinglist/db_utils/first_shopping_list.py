# -*- coding: utf-8 -*-
# __author__ = ‘du‘
# __created_at__ = '2017/12/12'
"""顶级品类菜单辅助函数"""

from shoppinglist.models import FirstShoppingList


def get_first_shopping_list_context():
    """
    获取所有的一级品类菜单数据
    :return:
    """
    return {
        'first_shopping_list': FirstShoppingList.get_items()
    }
