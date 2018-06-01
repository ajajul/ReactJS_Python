# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-17 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0041_address_is_gift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, help_text='(65xxxxxxxx)', max_length=10, verbose_name='Phone'),
        ),
    ]