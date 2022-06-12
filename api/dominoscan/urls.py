from rest_framework.routers import DefaultRouter
from .views import DominoViewSet
from django.urls import path
from django.conf.urls import include


router = DefaultRouter()
router.register('', DominoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
