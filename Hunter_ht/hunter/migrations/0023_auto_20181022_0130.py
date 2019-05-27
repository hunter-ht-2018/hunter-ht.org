# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0022_auto_20181016_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='editDateTime',
            field=models.DateField(default=datetime.date(2018, 10, 22)),
        ),
    ]
