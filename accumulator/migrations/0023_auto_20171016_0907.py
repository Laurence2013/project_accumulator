# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accumulator', '0022_auto_20171016_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='williamhilldailymatche',
            name='wh_csv_links',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
    ]