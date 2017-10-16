# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games_odds', '0025_williamhillgames1_williamhillodds1'),
        ('accumulator', '0015_remove_williamhilldailymatche_wh_csv_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='williamhilldailymatche',
            name='wh_csv_links',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
            preserve_default=False,
        ),
    ]
