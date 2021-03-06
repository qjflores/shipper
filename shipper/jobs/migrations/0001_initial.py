# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 09:06
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(max_length=5)),
                ('status', models.IntegerField(blank=True, choices=[(0, b'unknown'), (1, b'requested'), (2, b'booked'), (3, b'pickup'), (4, b'enroute'), (5, b'drop'), (6, b'fulfilled')], default=0, null=True)),
                ('pickup_location', django.contrib.gis.db.models.fields.PointField(dim=3, srid=4326)),
                ('drop_location', django.contrib.gis.db.models.fields.PointField(dim=3, srid=4326)),
                ('time_to_reach', models.IntegerField()),
                ('amount_offered', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
