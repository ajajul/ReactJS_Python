# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-15 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0037_coffeereview_brew'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeereview',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]