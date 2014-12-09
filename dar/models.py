from django.db import models
from django_enumfield import enum

class SecretariatStyle(enum.Enum):
    GRADUATION = 0
    POSTGRADUATE = 1

class DisciplineStyle(enum.Enum):
    ELECTIVE = 0
    MANDATORY = 1
    NOTOFFERED = 0
    OFFERED = 1

class Departament(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%d: %s' % (self.id, self.name)

class Secretariat(models.Model):
    type = enum.EnumField(SecretariatStyle)
    name = models.CharField(max_length=100)
    departament = models.ForeignKey(Departament, related_name='secretariat', null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%d: %s' % (self.id, self.name)

class Course(models.Model):
    name = models.CharField(max_length=100)
    secretariat = models.ForeignKey(Secretariat, related_name='course', null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%d: %s' % (self.id, self.name)

class Discipline(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    number_credit = models.IntegerField(default=0)
    required = enum.EnumField(DisciplineStyle, default=DisciplineStyle.MANDATORY)
    offered = enum.EnumField(DisciplineStyle, default=DisciplineStyle.NOTOFFERED)
    period_offered = models.DateField(null=True)
    required_credit = models.IntegerField(blank=True, null=True)
    teacher = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='discipline', null=True)
    departament = models.ForeignKey(Departament, related_name='discipline', null=True)
    disciplines = models.ManyToManyField('self', related_name='dscipline_req', null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%d: %s' % (self.id, self.name)

class Student(models.Model):
    name = models.CharField(max_length=100)
    matriculation = models.IntegerField(blank=True, null=True, unique=True)
    credit_mandatory = models.IntegerField(blank=True, null=True)
    credit_elective = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(Course, related_name='student', null=True)
    departament = models.ForeignKey(Departament, related_name='student', null=True)
    disciplines = models.ManyToManyField(Discipline, null=True, blank=True)
    matriculate = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%d: %s' % (self.id, self.name)