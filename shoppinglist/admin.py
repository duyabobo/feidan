# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.


class FirstShoppingListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'serial_number')
    search_fields = ('id', 'name')


admin.site.register(FirstShoppingList, FirstShoppingListAdmin)
