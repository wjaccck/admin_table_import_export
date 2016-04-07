from django.conf.urls import patterns, url
from info_api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'item', views.ItemViewSet)
router.register(r'location', views.LocationViewSet)
router.register(r'env', views.EnvViewSet)
router.register(r'list', views.ListViewSet)
router.register(r'version', views.VersionViewSet)

urlpatterns = router.urls
