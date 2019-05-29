# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0006_auto_20180906_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='index',
            field=models.CharField(default=b' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='publications',
            name='journalname',
            field=models.CharField(default=b' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='publications',
            name='messages',
            field=models.CharField(default=b'no information', max_length=1000),
        ),
    ]
