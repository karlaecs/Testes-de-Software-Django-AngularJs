from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter

from dar import views

urlpatterns = patterns(
    'dar.views',
    url(r'^$', 'index'),

    #api
    url(r'^api/students/$', views.StudentList.as_view()),
    url(r'^api/disciplines/$', views.DisciplineList.as_view()),
    url(r'^api/secretariats/$', views.SecretariatList.as_view()),

    url(r'^api/disciplines/departament/$', 'list_by_departament', name='list_by_departament'),
    #url(r'edit-offer/(?P<id>\d+)/$', 'DisciplineList.list_by_departament', name='list_by_departament'),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)
