# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0008_auto_20160203_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph.TimeSeries'),
        ),
    ]
