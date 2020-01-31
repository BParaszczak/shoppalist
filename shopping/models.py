import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import now

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

    name = models.CharField(max_length=30)
    amount = models.FloatField(blank=True, default=0)
    unit = models.CharField(max_length=6, choices=UNITS, default='pcs') #tu rozwijana lista z jednostkami: pcs, kg, l, box, bottle, dag
    comment = models.CharField(max_length=100, blank=True, default='-')
    # add_date = models.DateTimeField(, verbose_name="Added")
    urgency = models.CharField(max_length=10, verbose_name="Urgent", choices=URGENT, default='no')
    categories = models.ManyToManyField(
        'Category', 
        through='Entry',
        through_fields=('product', 'category'), 
        blank=False,
        )

    owner = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, default='All')

    def __str__(self):
        return f"{self.product_name} {self.amount} {self.unit} {self.comment}"

    def get_absolute_url(self):
        return reverse('name', args=[self.pk])
    
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

    def __str__(self):
        return self.name

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