# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0005_auto_20180906_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
