# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 20:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20161111_0659'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KirrURLManager',
        ),
    ]
