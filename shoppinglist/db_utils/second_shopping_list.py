# -*- coding: utf-8 -*-
# __author__ = ‘du‘
# __created_at__ = '2017/12/18'
"""二级品类菜单辅助函数"""

from shoppinglist.models import SecondShoppingList


def get_second_shopping_list_context(first_shopping_item_id):
    """
    获取所有的二级品类菜单数据
    :param first_shopping_item_id: 顶级菜单id
    :return:
    """
    return {
        'second_shopping_list': SecondShoppingList.get_items_by_father_id(father_id=first_shopping_item_id)
    }
