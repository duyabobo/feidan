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
    first_shopping_lists = FirstShoppingList.get_items()
    first_shopping_list_context = {
        f_s_l.serial_number: f_s_l.name for f_s_l in first_shopping_lists
    }
    sorted_list = map(  # 排个序
        lambda x:
        x[1],
        sorted(first_shopping_list_context.items(), key=lambda item: item[0])
    )
    return {'first_shopping_list': sorted_list}
