# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0023_auto_20181022_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='introduction',
            field=models.TextField(default=b'No Information'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='editDateTime',
            field=models.DateField(default=datetime.date(2018, 10, 31)),
        ),
    ]
