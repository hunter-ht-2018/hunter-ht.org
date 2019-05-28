# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0017_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='editDateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='articles',
            name='publish',
            field=models.CharField(default=b'0', max_length=5),
        ),
    ]
