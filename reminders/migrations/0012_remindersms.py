# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-24 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0040_auto_20170925_0348'),
        ('reminders', '0011_auto_20170906_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReminderSMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='6588222121', max_length=12)),
                ('message', models.CharField(default='Hookcoffee test message by Evgeny #4', max_length=612)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('scheduled', models.DateTimeField()),
                ('sent', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
            ],
        ),
    ]