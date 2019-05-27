# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0014_pubtouser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='identity',
            field=models.CharField(default=b'0', max_length=1),
        ),
    ]
