"""
Definition of models.
"""

from django.db import models

# Create your models here.

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
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name='Из коллекции')
    cost = models.PositiveIntegerField(verbose_name='Цена')

