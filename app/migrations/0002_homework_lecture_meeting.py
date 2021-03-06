# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('issue_date', models.CharField(max_length=10)),
                ('submission_date', models.CharField(max_length=10)),
                ('task_text', models.CharField(max_length=500)),
                ('file_name', models.CharField(max_length=50)),
                ('file_source', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('file_name', models.CharField(max_length=50)),
                ('file_source', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
