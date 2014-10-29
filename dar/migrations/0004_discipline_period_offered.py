# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dar', '0003_auto_20141029_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='discipline',
            name='period_offered',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
