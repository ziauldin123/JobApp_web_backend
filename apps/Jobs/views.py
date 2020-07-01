from rest_framework import serializers, viewsets, routers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Job

# Serializers define the API representation.
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'jtype', 'category', 'post_image', 'last_date','company_name', 'company_description', 'website', 'created_at', 'status', 'posts', 'required_exp']
        # fields = '__all__'
        list_display = ['title', 'description', 'location', 'jtype', 'category', 'post_image', 'last_date','company_name', 'company_description', 'website', 'created_at', 'status', 'posts', 'required_exp']


# ViewSets define the view behavior.
class JobViewSet(viewsets.ModelViewSet):
    serializer_class=JobSerializer
    queryset = Job.objects.all()
    
    

class JobTypeView(generics.ListAPIView):
    serializer_class=JobSerializer
    queryset = Job.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']