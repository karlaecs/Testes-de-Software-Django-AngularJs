from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from rest_framework import permissions, viewsets

from dar.models import Course, Discipline, Departament, Student, Secretariat
from dar.serializers import CourseSerializer, DepartamentSerializer, DisciplineSerializer, SecretariatSerializer, StudentSerializer


@csrf_protect
@ensure_csrf_cookie
def index(request):
   return render(request, 'dar/index.html')


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class DepartamentViewSet(viewsets.ModelViewSet):
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class SecretariatViewSet(viewsets.ModelViewSet):
    queryset = Secretariat.objects.all()
    serializer_class = SecretariatSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #permissions_classes = (permissions.IsAuthenticatedOrReadOnly)