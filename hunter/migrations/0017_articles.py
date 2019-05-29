# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0016_publications_publishtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('articleID', models.BigIntegerField(serialize=False, primary_key=True)),
                ('authorID', models.IntegerField()),
                ('title', models.CharField(default=b' ', max_length=500)),
                ('content', models.TextField()),
                ('publish', models.IntegerField(default=0)),
            ],
        ),
    ]
