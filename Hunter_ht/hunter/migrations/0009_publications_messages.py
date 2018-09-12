# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0008_remove_publications_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='messages',
            field=models.CharField(default=b'no information', max_length=20),
        ),
    ]
