# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0013_auto_20180912_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='PubToUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pubID', models.BigIntegerField()),
                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]
