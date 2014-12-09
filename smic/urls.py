from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter

from dar import views

urlpatterns = patterns(
    'dar.views',
    url(r'^$', 'index'),

    #api
    #url(r'^api/', include(router.urls)),
    url(r'^api/students/$', views.StudentList.as_view()),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)
