# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_enumfield.db.fields
import django_enumfield.enum
import dar.models


class Migration(migrations.Migration):

    dependencies = [
        ('dar', '0002_auto_20141029_0352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secretariat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', django_enumfield.db.fields.EnumField(default=0, enum=dar.models.SecretariatStyle, choices=[(0, django_enumfield.enum.Value(b'GRADUATION', 0, b'GRADUATION', dar.models.SecretariatStyle)), (1, django_enumfield.enum.Value(b'POSTGRADUATE', 1, b'POSTGRADUATE', dar.models.SecretariatStyle))])),
                ('departament', models.ForeignKey(related_name=b'secretariat', to='dar.Departament', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='course',
            name='departament',
        ),
        migrations.RemoveField(
            model_name='departament',
            name='secretariat',
        ),
        migrations.AddField(
            model_name='course',
            name='secretariat',
            field=models.ForeignKey(related_name=b'course', to='dar.Secretariat', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='matriculation',
            field=models.IntegerField(unique=True, null=True, blank=True),
        ),
    ]
