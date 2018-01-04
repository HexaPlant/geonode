# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '24_to_26'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcebase',
            name='denominator',
            field=models.IntegerField(default=0, verbose_name='denominator'),
        ),
    ]
