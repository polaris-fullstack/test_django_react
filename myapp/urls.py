from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ItemViewSet, ContactViewSet, ObjectViewSet, PropertyViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'objects', ObjectViewSet)
router.register(r'properties', PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 