# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20160214_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='category.Category'),
        ),
    ]
