# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 08:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accumulator', '0014_williamhilldailymatche_wh_csv_links'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='williamhilldailymatche',
            name='wh_csv_links',
        ),
    ]
