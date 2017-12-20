# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.


class FirstShoppingListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'serial_number')
    search_fields = ('id', 'name')


class SecondShoppingListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'serial_number')
    search_fields = ('id', 'name')


class ThirdShoppingListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'serial_number')
    search_fields = ('id', 'name')


class SecondShoppingTagListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'serial_number')
    search_fields = ('id', 'name')


admin.site.register(FirstShoppingList, FirstShoppingListAdmin)
admin.site.register(SecondShoppingList, SecondShoppingListAdmin)
admin.site.register(ThirdShoppingList, ThirdShoppingListAdmin)
admin.site.register(SecondShoppingTagList, SecondShoppingTagListAdmin)
