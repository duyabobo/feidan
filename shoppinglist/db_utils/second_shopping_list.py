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
    second_shopping_lists = SecondShoppingList.get_items(first_shopping_item_id=first_shopping_item_id)
    second_shopping_list_context = {
        f_s_l.serial_number: f_s_l for f_s_l in second_shopping_lists
    }
    return {
        'second_shopping_list': map(
            lambda x: x[1], sorted(second_shopping_list_context.items(), key=lambda item: item[0])
        )
    }
