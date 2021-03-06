# Generated by Django 3.0.2 on 2020-01-29 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('amount', models.FloatField(max_length=6)),
                ('unit', models.CharField(choices=[('pcs', 'szt.'), ('box', 'op.'), ('bottle', 'but.'), ('kg', 'kg'), ('dag', 'dag'), ('l', 'l'), ('cm', 'cm'), ('m', 'm')], max_length=6)),
                ('comment', models.CharField(max_length=100)),
                ('need_date', models.DateTimeField(verbose_name='Needed before:')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
