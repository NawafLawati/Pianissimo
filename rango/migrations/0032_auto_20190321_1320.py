# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-21 13:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0031_auto_20190321_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 21, 13, 20, 11, 911565)),
        ),
    ]
