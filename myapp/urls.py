from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ItemViewSet, ContactViewSet, ObjectViewSet, PropertyViewSet, QueryViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'objects', ObjectViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'query', QueryViewSet, basename='query')

urlpatterns = [
    path('', include(router.urls)),
]