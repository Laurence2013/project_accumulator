# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games_odds', '0020_auto_20170930_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='williamhillodds0',
            name='games',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillGames0'),
        ),
    ]
