import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.urls import reverse

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

    URGENT = [
        ('yes', 'Tak'),
        ('no', 'Nie')
    ]

    name = models.CharField(max_length=50, verbose_name="Nazwa")
    amount = models.FloatField(blank=True, default=0, verbose_name="Ilość")
    unit = models.CharField(max_length=6, choices=UNITS, default='pcs', verbose_name="Jednostka") #tu rozwijana lista z jednostkami: pcs, kg, l, box, bottle, dag
    comment = models.CharField(max_length=100, blank=True, default='-', verbose_name="Uwagi")
    # add_date = models.DateTimeField(, verbose_name="Added")
    urgency = models.CharField(max_length=10, verbose_name="Pilne", choices=URGENT, default='no')
    categories = models.ManyToManyField(
        'Category', 
        through='Entry',
        through_fields=('product', 'category'), 
        blank=True,
        verbose_name="Lista"
        )

    owner = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Prywatne")

    def __str__(self):
        return f"{self.name} {self.amount} {self.unit} {self.comment}"

    def get_absolute_url(self):
        return reverse('product', args=[self.pk])
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


# categories = shopping lists for eg. groceries, meds, sports& outdoor, etc.
class Category(models.Model):

    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Lista',
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', args=[self.pk])
    
    class Meta:
       verbose_name = 'Category'
       verbose_name_plural = 'Categories'

# data dodania produktu do aplikacji
class Entry(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    add_date = models.DateTimeField(verbose_name="Entry date", default=now)

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
        ordering = ['add_date']



# class User(models.Model):
#     user_name = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)