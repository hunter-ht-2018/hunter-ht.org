# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0027_auto_20181212_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='isPrivate',
            field=models.CharField(default=b'0', max_length=5),
        ),
        migrations.AlterField(
            model_name='articles',
            name='editDateTime',
            field=models.DateField(default=datetime.date(2019, 2, 25)),
        ),
    ]
