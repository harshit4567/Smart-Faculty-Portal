# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sslproject', '0020_auto_20171114_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='where',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
