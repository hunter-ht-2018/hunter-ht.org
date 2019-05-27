# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0012_auto_20180912_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pwd',
            field=models.CharField(max_length=100),
        ),
    ]
