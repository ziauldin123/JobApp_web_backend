from django.urls import path,include
from rest_framework import routers
from .views import JobViewSet


router = routers.DefaultRouter()
router.register(r'Api', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]