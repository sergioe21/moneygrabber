# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 03:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0006_auto_20160201_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oilpricedaily',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]