from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReportViewSet, LocationViewSet

router = DefaultRouter()
router.register(r'reports', ReportViewSet, basename='report')
router.register(r'locations', LocationViewSet, basename='location')

urlpatterns = [
    path('', include(router.urls)),
]
