# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-04 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games_odds', '0025_williamhillgames1_williamhillodds1'),
        ('accumulator', '0024_williamhillgameswithodds0'),
    ]

    operations = [
        migrations.AddField(
            model_name='williamhillgameswithodds0',
            name='games',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillGames0'),
        ),
    ]
