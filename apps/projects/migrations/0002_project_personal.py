# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='personal',
            field=models.BooleanField(default=False),
        ),
    ]
