# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 14:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170824_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
