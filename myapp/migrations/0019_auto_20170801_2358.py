# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20170801_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
