# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20171125_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='submission_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(),
        ),
    ]
