# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0009_publications_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='messages',
            field=models.CharField(default=b'no information', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='pwd',
            field=models.CharField(max_length=100),
        ),
    ]
