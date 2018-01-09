# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-09 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accumulator', '0030_coralgames0'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoralOdds0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_odds', models.DecimalField(decimal_places=2, max_digits=5)),
                ('draw_odds', models.DecimalField(decimal_places=2, max_digits=5)),
                ('away_odds', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('games', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accumulator.CoralDailyMatche')),
            ],
        ),
    ]
