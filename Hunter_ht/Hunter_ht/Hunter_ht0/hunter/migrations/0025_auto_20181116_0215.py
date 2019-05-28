# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0024_auto_20181031_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='isOpen',
            field=models.CharField(default=b'1', max_length=5),
        ),
        migrations.AddField(
            model_name='publications',
            name='uploadByUser',
            field=models.CharField(default=b'no recording', max_length=50),
        ),
        migrations.AlterField(
            model_name='articles',
            name='editDateTime',
            field=models.DateField(default=datetime.date(2018, 11, 16)),
        ),
        migrations.AlterField(
            model_name='pubtouser',
            name='username',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='nake_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
