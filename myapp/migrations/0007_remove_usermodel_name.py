# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 22:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_commentmodel_likemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='name',
        ),
    ]