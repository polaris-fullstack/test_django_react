from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ItemViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 