# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_odds', '0004_auto_20170920_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeofrefreshwilliamhill0',
            name='william_hill_id',
            field=models.CharField(max_length=100),
        ),
    ]