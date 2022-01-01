# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CyStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('stat_dt', models.CharField(max_length=10)),
                ('cy_name', models.CharField(max_length=50)),
                ('confirm', models.IntegerField()),
                ('dead', models.IntegerField()),
                ('heal', models.IntegerField()),
                ('today_confirm', models.IntegerField()),
                ('today_new_confirm', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProvStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('stat_dt', models.CharField(max_length=10)),
                ('cy_name', models.CharField(max_length=50)),
                ('prov_name', models.CharField(max_length=50)),
                ('confirm', models.IntegerField()),
                ('dead', models.IntegerField()),
                ('heal', models.IntegerField()),
                ('today_confirm', models.IntegerField()),
                ('today_new_confirm', models.IntegerField()),
            ],
        ),
    ]
