# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-07 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_shared_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shared_notes',
            name='n_shrd_owner',
            field=models.CharField(max_length=20),
        ),
    ]
