# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('pubID', models.BigIntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=1000)),
            ],
        ),
    ]
