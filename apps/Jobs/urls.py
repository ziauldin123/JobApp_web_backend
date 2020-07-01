from django.urls import path,include
from rest_framework import routers
from .views import JobViewSet,JobTypeView

router = routers.DefaultRouter()
router.register(r'', JobViewSet)


# job_router = routers.NestedSimpleRouter(router, r'', lookup='category')
# job_router.register(r'',JobTypeView, basename='category')


urlpatterns = [
    path('job', JobTypeView.as_view()),
    # path('', include(router.urls)),
    
]