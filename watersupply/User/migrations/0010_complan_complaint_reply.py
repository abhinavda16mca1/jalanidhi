# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-01 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_auto_20190329_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='complan',
            name='Complaint_Reply',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
