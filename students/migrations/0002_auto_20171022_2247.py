# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-22 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='id',
        ),
        migrations.AlterField(
            model_name='marks',
            name='assn_max_marks',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='marks',
            name='suser_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='students.student'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='test1_max_marks',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='marks',
            name='test2_max_marks',
            field=models.IntegerField(default=15),
        ),
    ]