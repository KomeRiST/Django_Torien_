"""
Definition of models.
"""

from django.db import models
from app import fields

# Create your models here.

class Gallery(models.Model):
    '''
    Галерея для конкретного товара
    '''
    image = models.ImageField(upload_to='gallery')
    thing = models.ForeignKey('Thing', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.thing.name

    class Meta:
        verbose_name = 'Галерея товара'
        verbose_name_plural = 'Галерея товаров'

class Collection(models.Model):
    '''
    Коллекция одежды
    Хранит название, описание, картинку, дату создания
    '''
    name = models.CharField(max_length=50, verbose_name='Название коллекции')
    description = models.CharField(max_length=250, verbose_name='Описание коллекции')
    image = models.ImageField(verbose_name='Общее фото коллекции')
    data_create = models.DateField(verbose_name='Дата создания коллекции')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция одежды'
        verbose_name_plural = 'Коллекции одежды'


class Category(models.Model):
    '''
    Категория товара
    (Платья, брюки, юбки, куртки и т.д.)
        Иконка
        Название
    '''
    icon = models.ImageField(upload_to='category_icon', verbose_name='Иконка категории')
    name = models.CharField(max_length=50, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Thing(models.Model):
    '''
    Товар (конекретная вещ, которую можно заказать)
    Хранит: 
        тип товара(платье, рубашка и т.д.)
        фото товара
        описание (не обязательно)
        размеры
        цвета (в каких цветах имеется товар, в зависимости от размера)
        стоимость
    '''
    name = models.CharField(max_length=50, verbose_name='Название товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    #image = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='Изображения товара', related_name='images')
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name='Из коллекции')
    cost = models.PositiveIntegerField(verbose_name='Цена')
    color = fields.ColorField('Цвет обложки', default='#FF0000')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

