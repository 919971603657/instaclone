# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20170801_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(default='123', max_length=40),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(default='abc', max_length=120),
        ),
    ]
