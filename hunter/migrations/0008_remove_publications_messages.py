# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0007_auto_20180906_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publications',
            name='messages',
        ),
    ]
