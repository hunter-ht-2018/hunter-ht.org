# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0019_auto_20181016_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='editDateTime',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
