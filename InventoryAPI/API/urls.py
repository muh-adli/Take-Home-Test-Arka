from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import inventoryJson, inventoryRest, inventoryXml, homepage

router = DefaultRouter()
router.register(r'v1/inventory/rest', inventoryRest, basename='inventoryRest')

urlpatterns = [
    path('v1/inventory/json/', inventoryJson, name='inventoryJson'),
    path('v1/inventory/xml/', inventoryXml, name='inventoryXml'),
    path('', include(router.urls)),
]