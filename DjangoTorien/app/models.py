"""
Definition of models.
"""

from django.db import models
from app import fields
from colorfield.fields import ColorField
from PIL import Image, ImageFilter
from transliterate import translit
import os
# Create your models here.

class Gallery(models.Model):
    '''
    Галерея для конкретного товара
    '''
    name = models.CharField(max_length=25, blank=True, verbose_name='Название фотки')
    image = models.ImageField(upload_to='gallery')
    thing = models.ForeignKey('Thing', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.thing.name

    class Meta:
        verbose_name = 'Галерея товара'
        verbose_name_plural = 'Галерея товаров'


class Size(models.Model):
    '''
    Размер для вещей
    '''
    #Text = models.CharField(max_length=50, verbose_name='Краткое название')
    #thing = models.ForeignKey('Thing', on_delete=models.CASCADE, related_name='size')
    rus = models.PositiveIntegerField(verbose_name='Русский размер')
    all = models.CharField(max_length=7, verbose_name='Международный размер')

    def __str__(self):
        return "{} - [{}]".format(self.rus, self.all)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Color(models.Model):
    '''
    Цвет/а
    '''
    name = models.CharField(max_length=15, verbose_name='Название цвета')
    value = ColorField(default='#FFFFFF')

    def __str__(self):
        return "{} - [{}]".format(self.name, self.value)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

def translite(instance, filename):
    return 'collections/{0}/original.jpg'.format(translit(instance.name, 'ru', reversed=True))

class Collection(models.Model):
    '''
    Коллекция одежды
    Хранит название, описание, картинку, дату создания
    '''
    name = models.CharField(max_length=50, verbose_name='Название коллекции')
    description = models.CharField(max_length=250, verbose_name='Описание коллекции')
    image = models.ImageField(upload_to=translite, verbose_name='Общее фото коллекции')
    data_create = models.DateField(verbose_name='Дата создания коллекции')

    def __str__(self):
        return self.name

    @property
    def image_blur(self):
        return 'collections/{0}/blur.jpg'.format(translit(self.name, 'ru', reversed=True))

    def save(self, *args, **kwargs):
		# Сначала - обычное сохранение
        super(Collection, self).save(*args, **kwargs)
		# Для начала проверим наличие картинки
        if self.image:
			# Начинаем процедуру размытия картинки
            path = self.image.path
            img = Image.open(path)
            newimg = img.copy()
            newimg = img.filter(ImageFilter.GaussianBlur(radius=7))
            filename = os.path.dirname(path)+'\\blur.jpg'
            newimg.save(filename)


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

    @property
    def haveSize(self, s):
        r = Relationship.objects.filter(size=s)
        if r.count() > 0:
            return True
        else:
            return False

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='categories')
    #image = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='Изображения товара', related_name='images')
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name='Из коллекции')
    cost = models.PositiveIntegerField(verbose_name='Цена')
    #color = models.ManyToManyField(Color)
    #color = fields.ColorField('Цвет обложки', default='#FF0000')
    #size = models.ManyToManyField(Size)
    date_add = models.DateField(verbose_name='Дата добавления',auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def random_image(self):
        glr = Gallery.objects.filter(thing=self.id).order_by('?')[:1]
        if glr.count() == 0:
            return "/gallery/default.jpg"
        r = glr[0].image
        #glr = Gallery.objects.get(thing=self.id)
        #print(glr)
        #print(glr.image)
        #print(glr[0])
        return r

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Relationship(models.Model):
    thing = models.ForeignKey(Thing, related_name='things')
    size = models.ForeignKey(Size, related_name='sizes')
    color = models.ForeignKey(Color, related_name='colors')
    count = models.PositiveIntegerField(verbose_name='Количество', default=1)
    sale = models.PositiveIntegerField(verbose_name='Количество проданных', default=0)
    favorite = models.PositiveIntegerField(verbose_name='Количество заказанных', default=0)