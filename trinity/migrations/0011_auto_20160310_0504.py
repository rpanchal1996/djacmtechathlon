# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 23:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trinity', '0010_teststart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='no_of_sub',
        ),
        migrations.RemoveField(
            model_name='question',
            name='time_posted',
        ),
    ]
