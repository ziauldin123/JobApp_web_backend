from rest_framework import serializers, viewsets, routers
from .models import Job

# Serializers define the API representation.
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['title','description','location','type','category','last_date','company_name','company_description','website','created_at','filled','salary','required_exp']
        list_display = ['title','description','location','type','category','last_date','company_name','company_description','website','created_at','filled','salary','required_exp']


# ViewSets define the view behavior.
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer