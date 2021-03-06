# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-13 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_odds', '0025_williamhillgames1_williamhillodds1'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoralCsvLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(max_length=50)),
                ('get_match_odds_link_csv', models.CharField(max_length=100)),
                ('ids_for_tag_span_link_csv', models.CharField(max_length=100)),
                ('ids_for_tag_tbody_link_csv', models.CharField(max_length=100)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
