# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trinity', '0002_question_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='proceed',
            field=models.IntegerField(default=0),
        ),
    ]
