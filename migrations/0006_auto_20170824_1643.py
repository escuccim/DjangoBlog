# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170824_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
