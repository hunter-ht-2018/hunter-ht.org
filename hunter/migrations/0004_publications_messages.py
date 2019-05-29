# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0003_auto_20180904_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='messages',
            field=models.CharField(max_length=1000, null=b'no information'),
        ),
    ]
