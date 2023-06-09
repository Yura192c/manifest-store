import re
from decimal import Decimal

from django.db import models
from django.urls import reverse
import requests
from django.core.exceptions import ValidationError
from parser.parser import parse_NB, update_price_NB


class dollarRate(models.Model):
    '''Курс доллара'''
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.rate)

    class Meta:
        verbose_name = 'Курс доллара'
        verbose_name_plural = 'Курс доллара'


class Manufacturer(models.Model):
    '''Производитель'''
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_manufacturer',
                       args=[self.slug])


class Category(models.Model):
    '''Категория'''
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    hender = {
        ('M', 'Мужской'),
        ('W', 'Женский'),
        ('K', 'Детский'),
        ('ALL', 'Все')
    }
    hender = models.CharField(max_length=3, choices=hender, default='ALL')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    manufacturer = models.ForeignKey(Manufacturer, related_name='products', on_delete=models.PROTECT)
    url = models.URLField(null=True, blank=False, help_text='Ссылка на товар на другом сайте')
    image_urs = models.JSONField(null=True, blank=True)
    sizes = models.JSONField(null=True, blank=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    dollarRate = models.ForeignKey(dollarRate, related_name='products', on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=10, null=True, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """ Переопередение метода сохранения для заполнения данных модели данными из сайта-донора"""
        if not Product.objects.filter(name=self.name).exists():

            if self.url:
                # Получение данных с другого сайта
                if self.manufacturer.name == "New Balance":
                    data = parse_NB(self.url)
                # Получение цены из данных
                price = data['price']
                images = data['images']
                sizes = data['sizes']
                sizes_json = {}
                images_json = {}
                for url in images:
                    images_json[f'image{len(images_json)}'] = url
                for size in sizes:
                    sizes_json[f'size{len(sizes_json)}'] = size
                self.sizes = sizes_json
                self.image_urs = images_json
                # Сохранение цены в поле price
                # цена = цена * курс доллара + 20% от цены

                self.price = Decimal(
                    Decimal(str(price)) * self.dollarRate.rate + Decimal(str(price / 100 * 20))).quantize(
                    Decimal('.01'))
                self.name = data['name']
                self.description = data['description']

                self.slug = create_slug(data['name'])

        super(Product, self).save(*args, **kwargs)

    def update_product_price(self):
        """Обновление цены товара"""
        price = update_price_NB(self.url)
        self.price = Decimal(Decimal(str(price)) * self.dollarRate.rate + Decimal(str(price / 100 * 20))).quantize(
            Decimal('.01'))

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.category.slug, self.id, self.slug])


def create_slug(name: str) -> str:
    slug = name.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_-]+', '-', slug)
    slug = re.sub(r'^-+|-+$', '', slug)
    return slug
