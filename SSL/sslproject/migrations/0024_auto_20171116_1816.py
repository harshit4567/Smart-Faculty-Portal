# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sslproject', '0023_achievements_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teaching',
            name='end_date',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='start_date',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]