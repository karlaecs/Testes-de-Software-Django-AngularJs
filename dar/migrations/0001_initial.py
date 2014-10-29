# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_enumfield.db.fields
import django_enumfield.enum
import dar.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('secretariat', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('number_credit', models.IntegerField(default=0)),
                ('required', django_enumfield.db.fields.EnumField(default=1, enum=dar.models.DisciplineStyle, choices=[(0, django_enumfield.enum.Value(b'ELECTIVE', 0, b'ELECTIVE', dar.models.DisciplineStyle)), (1, django_enumfield.enum.Value(b'OFFERED', 1, b'OFFERED', dar.models.DisciplineStyle))])),
                ('offered', django_enumfield.db.fields.EnumField(default=0, enum=dar.models.DisciplineStyle, choices=[(0, django_enumfield.enum.Value(b'ELECTIVE', 0, b'ELECTIVE', dar.models.DisciplineStyle)), (1, django_enumfield.enum.Value(b'OFFERED', 1, b'OFFERED', dar.models.DisciplineStyle))])),
                ('required_credit', models.IntegerField(null=True, blank=True)),
                ('teacher', models.CharField(max_length=100)),
                ('course', models.ForeignKey(related_name=b'discipline', to='dar.Course')),
                ('pre_discipline', models.ForeignKey(related_name=b'prediscline', blank=True, to='dar.Discipline', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('matriculation', models.IntegerField(null=True, blank=True)),
                ('credit_mandatory', models.IntegerField(null=True, blank=True)),
                ('credit_elective', models.IntegerField(null=True, blank=True)),
                ('departament', models.ForeignKey(related_name=b'student', to='dar.Departament')),
                ('discipline', models.ForeignKey(related_name=b'student', to='dar.Discipline')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='departament',
            field=models.ForeignKey(related_name=b'course', to='dar.Departament'),
            preserve_default=True,
        ),
    ]
