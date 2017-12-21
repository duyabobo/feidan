# -*- coding: utf-8 -*-
# __author__ = ‘du‘
# __created_at__ = '2017/12/18'

from shoppinglist.models import ThirdShoppingList, ONE_PAGE_LIMIT


def get_third_shopping_list_context(second_shopping_item_id, page=0):
    """
    获取某一类二级菜单下的一批三级菜单
    :param second_shopping_item_id: 某个二级菜单的id
    :param page:
    :return:
    """
    return {
        'third_shopping_list':
            ThirdShoppingList.get_items_by_father_id(father_id=second_shopping_item_id, page=page, limit=ONE_PAGE_LIMIT)
    }


def get_third_shopping_list_total(second_shopping_item_id):
    """
    获取某一类二级菜单下的三级菜单总数
    :param second_shopping_item_id:
    :return:
    """
    return ThirdShoppingList.get_total(father_id=second_shopping_item_id)
