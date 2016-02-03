# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 03:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0004_auto_20160201_0343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oilpricedaily',
            name='day',
        ),
        migrations.RemoveField(
            model_name='oilpricedaily',
            name='month',
        ),
        migrations.RemoveField(
            model_name='oilpricedaily',
            name='year',
        ),
        migrations.AddField(
            model_name='oilpricedaily',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
