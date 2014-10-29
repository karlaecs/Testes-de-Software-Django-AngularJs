# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='departament',
            field=models.ForeignKey(related_name=b'course', to='dar.Departament', null=True),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='course',
            field=models.ForeignKey(related_name=b'discipline', to='dar.Course', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='departament',
            field=models.ForeignKey(related_name=b'student', to='dar.Departament', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='discipline',
            field=models.ForeignKey(related_name=b'student', to='dar.Discipline', null=True),
        ),
    ]
