from django import forms
from django.forms import SelectMultiple

from .models import Product, Category, Entry


class AddProductForm(forms.Form):
    """Formularz wprowadzania produktu"""


class DeleteSelectedForm(forms.Form):
    """Form for selecting products to delete from the list"""
    products = forms.ModelMultipleChoiceField(
                    widget = forms.CheckboxSelectMultiple,
                    queryset = Product.objects.all(),
    )
