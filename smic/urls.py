from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter

from dar import views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'departaments', views.DepartamentViewSet)
router.register(r'disciplines', views.DisciplineViewSet)
router.register(r'secretariats', views.SecretariatViewSet)

urlpatterns = patterns('',
                       url(r'^api/', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^$', views.index, name='index'),
)
