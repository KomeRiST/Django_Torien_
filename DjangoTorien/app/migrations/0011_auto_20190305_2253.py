# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-05 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190305_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='favorite',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество заказанных'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='sale',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество проданных'),
        ),
    ]