# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0015_user_identity'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='publishType',
            field=models.CharField(default=b' ', max_length=100),
        ),
    ]
