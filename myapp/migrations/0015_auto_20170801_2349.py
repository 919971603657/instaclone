# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20170801_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
    ]
