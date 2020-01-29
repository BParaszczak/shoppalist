import datetime

from django.db import models
from django.utils import timezone

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

    name = models.CharField(max_length=30)
    amount = models.FloatField(max_value=100)
    unit = models.CharField(max_length=6, choices=UNITS, default='pcs') #tu rozwijana lista z jednostkami: pcs, kg, l, box, bottle, dag
    comment = models.CharField(max_length=100)
    # add_date = models.DateTimeField(, verbose_name="Added")
    need_date = models.DateTimeField(verbose_name="Needed before")
    categories = models.ManyToManyField('Category', blank=False)

    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.product_name} {self.amount} {self.unit} {self.comment}"
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


# categories = shopping lists for eg. groceries, meds, sports& outdoor, etc.
class Category(models.Model):

    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Category',
    )

    class Meta:
       verbose_name = 'Category'
       verbose_name_plural = 'Categories'


class Added(models.Model):

    product = models.ForeignKey('Product')
    category = models.ForeignKey('Category')
    add_date = models.DateTimeField(verbose_name="Added")


# class User(models.Model):
#     user_name = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)