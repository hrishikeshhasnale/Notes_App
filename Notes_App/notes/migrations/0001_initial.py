# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-07 07:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserMgnt', '0002_notes_owner_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
  
    ]
