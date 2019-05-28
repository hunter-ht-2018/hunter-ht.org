# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0026_auto_20181116_0215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publications',
            old_name='index',
            new_name='indexType',
        ),
        migrations.AlterField(
            model_name='articles',
            name='editDateTime',
            field=models.DateField(default=datetime.date(2018, 12, 12)),
        ),
    ]
