# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 18:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('intake', '0004_auto_20170508_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]