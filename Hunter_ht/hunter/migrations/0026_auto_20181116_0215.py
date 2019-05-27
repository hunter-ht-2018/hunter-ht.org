# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0025_auto_20181116_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='uploadByUser',
            field=models.CharField(default=b'no records', max_length=50),
        ),
    ]
