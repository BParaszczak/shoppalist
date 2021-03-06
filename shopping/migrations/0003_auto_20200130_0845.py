# Generated by Django 3.0.2 on 2020-01-30 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping', '0002_auto_20200129_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='need_date',
        ),
        migrations.AddField(
            model_name='product',
            name='urgency',
            field=models.CharField(choices=[('yes', 'Tak'), ('no', 'Nie')], default='no', max_length=10, verbose_name='Urgent'),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(through='shopping.Entry', to='shopping.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='comment',
            field=models.CharField(blank=True, default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
