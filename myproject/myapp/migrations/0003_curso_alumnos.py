# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20170406_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='alumnos',
            field=models.ManyToManyField(default='', to='myapp.Alumno'),
        ),
    ]
