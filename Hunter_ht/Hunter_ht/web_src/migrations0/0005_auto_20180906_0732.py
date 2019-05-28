# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0004_publications_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 9, 6, 7, 32, 44, 387753, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='publications',
            name='index',
            field=models.CharField(max_length=100, null=b'no information'),
        ),
        migrations.AddField(
            model_name='publications',
            name='journalname',
            field=models.CharField(max_length=1000, null=b'no information'),
        ),
    ]
