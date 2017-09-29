# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games_odds', '0018_williamhillurllinks_url_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='WilliamHillCsvLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(max_length=50)),
                ('get_match_odds_link_csv', models.CharField(max_length=100)),
                ('ids_for_tag_span_link_csv', models.CharField(max_length=100)),
                ('ids_for_tag_tbody_link_csv', models.CharField(max_length=100)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='williamhillgames0',
            name='url_game_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.AlterField(
            model_name='williamhillgames1',
            name='url_game_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.AlterField(
            model_name='williamhillgames2',
            name='url_game_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.AlterField(
            model_name='williamhillgames3',
            name='url_game_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.AlterField(
            model_name='williamhillgames4',
            name='url_game_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.AlterField(
            model_name='williamhillgames5',
            name='url_game_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.AlterField(
            model_name='williamhillgames6',
            name='url_game_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.AlterField(
            model_name='williamhillodds0',
            name='games',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.AlterField(
            model_name='williamhillodds1',
            name='games',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.AlterField(
            model_name='williamhillodds2',
            name='games',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.AlterField(
            model_name='williamhillodds3',
            name='games',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.AlterField(
            model_name='williamhillodds4',
            name='games',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.AlterField(
            model_name='williamhillodds5',
            name='games',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.AlterField(
            model_name='williamhillodds6',
            name='games',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_odds.WilliamHillCsvLinks'),
        ),
        migrations.DeleteModel(
            name='WilliamHillUrlLinks',
        ),
    ]
