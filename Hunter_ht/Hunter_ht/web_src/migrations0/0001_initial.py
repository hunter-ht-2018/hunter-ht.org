# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
                ('nake_name', models.CharField(max_length=50)),
            ],
        ),
    ]
