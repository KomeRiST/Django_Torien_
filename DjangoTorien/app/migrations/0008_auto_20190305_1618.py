# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-05 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190305_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='favorite',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество заказанных'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thing',
            name='sale',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество проданных'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='thing',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='app.Category', verbose_name='Категория'),
        ),
    ]
