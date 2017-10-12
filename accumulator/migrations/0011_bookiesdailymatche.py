# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accumulator', '0010_auto_20171010_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookiesDailyMatche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates_of_games', models.CharField(max_length=50)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('bookies_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accumulator.Bookie')),
            ],
        ),
    ]