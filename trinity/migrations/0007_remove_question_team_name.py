# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 22:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trinity', '0006_auto_20160310_0348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='team_name',
        ),
    ]
