from django.db import models
from django.contrib import admin


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', max_length=255, blank=True)


admin.site.register(Category)
admin.site.register(Product)
