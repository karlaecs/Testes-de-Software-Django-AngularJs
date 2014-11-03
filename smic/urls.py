from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
#from django.contrib import admin

from dar import views

#admin.autodiscover()

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'departaments', views.DepartamentViewSet)
router.register(r'disciplines', views.DisciplineViewSet)
router.register(r'secretariats', views.SecretariatViewSet)
##router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
                       #url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^$', views.index, name='index'),
)
