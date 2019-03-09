# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-05 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190305_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thing',
            name='count',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='favorite',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='sale',
        ),
        migrations.AddField(
            model_name='relationship',
            name='count',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='favorite',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество заказанных'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relationship',
            name='sale',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество проданных'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='thing',
            name='date_add',
            field=models.DateField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
    ]