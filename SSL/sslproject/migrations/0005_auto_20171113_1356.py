# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sslproject', '0004_auto_20171109_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='employee',
            name='current_institute',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='mobileNo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='year_of_joining',
            field=models.CharField(default='', max_length=100),
        ),
    ]
