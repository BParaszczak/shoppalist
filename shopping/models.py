import datetime

from django.db import models
from django.db import timezone
from django.form import ModelForms

from django.contrib.auth.models import User



# product added to shopping lists
class Product(models.Model):

    UNITS = [
        ('pcs', 'szt.'),
        ('box', 'op.'),
        ('bottle', 'but.'),
        ('kg', 'kg'),
        ('dag', 'dag'),
        ('l', 'l'),
        ('cm', 'cm'),
        ('m', 'm'),
    ]

    product_name = models.CharField(max_length=30)
    amount = models.FloatField(max_length=6)
    unit = models.CharField(max_length=5, choices=UNITS) #tu rozwijana lista z jednostkami: pcs, kg, l, box, bottle, dag
    comment = models.CharField(max_length=100)
    need_date = models.DateTimeField(verbose_name="Needed before:")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name = ('Product')
        verbose_name_plural = ('Products')


# categories = shopping lists for eg. groceries, meds, sports& outdoor, etc.
class Category(models.Model):

    category_name = models.CharField('Category', on_delete=models.CASCADE)
    max_length=30,
    unique=True,
    verbose_name=("Category"),

    class Meta:
       verbose_name = ('Category')
       verbose_name_plural = ('Categories')


# class User(models.Model):
#     user_name = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)