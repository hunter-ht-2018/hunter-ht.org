# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0002_publications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publications',
            old_name='author',
            new_name='authors',
        ),
    ]
