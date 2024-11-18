from django.db import models
from django.urls import reverse


class Categories(models.Model):
    title = models.CharField(max_length=200, verbose_name='Категории')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Продукт')
    price = models.FloatField(verbose_name='Цена')
    size = models.IntegerField(verbose_name='Размер')
    colour = models.CharField(max_length=200, verbose_name='Цвет')
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тип товара')
    details = models.TextField(max_length=300, verbose_name='Детали')
    slug = models.SlugField(unique=True, null=True)
    image = models.ImageField(upload_to='products/', verbose_name='Картинка товара')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

    def get_image_slider(self):
        if self.image:
            try:
                return self.image.url
            except:
                return '-'
        else:
            return '-'

    def get_image_product(self):
        if self.images:
            try:
                return self.images.first().image.url
            except:
                return '-'
        else:
            return '-'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Type(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тип товара')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'
