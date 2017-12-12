# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-12 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstShoppingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u8bb0\u5f55\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65e5\u671f')),
                ('name', models.CharField(default='', max_length=20, verbose_name='\u540d\u79f0')),
                ('serial_number', models.IntegerField(default=0, verbose_name='\u4f4d\u7f6e\u5e8f\u53f7')),
            ],
            options={
                'db_table': 't_first_shopping_list',
            },
        ),
    ]
