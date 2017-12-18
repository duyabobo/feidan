# -*- coding: utf-8 -*-
# __author__ = ‘du‘
# __created_at__ = '2017/12/18'

from shoppinglist.models import ThirdShoppingList


def get_third_shopping_list_context(second_shopping_item_id, page=0):
    """
    获取某一类二级菜单下的一批三级菜单
    :param second_shopping_item_id: 某个二级菜单的id
    :param page:
    :return:
    """
    third_shopping_lists = ThirdShoppingList.get_items_by_father_id(father_id=second_shopping_item_id, page=page, limit=24)
    third_shopping_list_context = {
        t_s_l.serial_number: t_s_l for t_s_l in third_shopping_lists
    }
    return {
        'third_shopping_list': map(
            lambda x: x[1], sorted(third_shopping_list_context.items(), key=lambda item: item[0])
        )
    }
