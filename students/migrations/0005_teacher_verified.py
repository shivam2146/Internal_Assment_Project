# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20171029_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
