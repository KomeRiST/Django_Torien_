# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-03 19:34
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Название цвета')),
                ('value', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'Размер', 'verbose_name_plural': 'Размеры'},
        ),
        migrations.RemoveField(
            model_name='size',
            name='Text',
        ),
        migrations.RemoveField(
            model_name='size',
            name='thing',
        ),
        migrations.AddField(
            model_name='thing',
            name='size',
            field=models.ManyToManyField(to='app.Size'),
        ),
        migrations.RemoveField(
            model_name='thing',
            name='color',
        ),
        migrations.AddField(
            model_name='thing',
            name='color',
            field=models.ManyToManyField(to='app.Color'),
        ),
    ]
