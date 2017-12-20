# -*- coding: utf-8 -*-
# __author__ = ‘du‘
# __created_at__ = '2017/12/20'

from shoppinglist.models import SecondShoppingTagList


def get_second_shopping_tag_list_context(second_shopping_item_id):
    """
    获取某一类二级菜单下的tag列表，显示前20个tag
    :param second_shopping_item_id: 某个二级菜单的id
    :param page:
    :return:
    """
    return {
        'second_shopping_tag_list':
            SecondShoppingTagList.get_items_by_father_id(father_id=second_shopping_item_id, limit=24)
    }
