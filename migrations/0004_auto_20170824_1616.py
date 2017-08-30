# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170824_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
