# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-21 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0008_remove_water_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='water',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='water',
            name='Desig',
        ),
        migrations.AddField(
            model_name='water',
            name='address',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='water',
            name='dob',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='water',
            name='gender',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='water',
            name='Email',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='water',
            name='Name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='water',
            name='Password',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='water',
            name='Phoneno',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='water',
            name='Status',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='water',
            name='Username',
            field=models.CharField(default='', max_length=30),
        ),
    ]
