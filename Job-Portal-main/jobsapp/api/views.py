from rest_framework import viewsets
from jobsapp.models import HydJobs 
from jobsapp.api.serialization import HydJobsSerializer

class HydJobsCRUDCBV(viewsets.ModelViewSet):
    serializer_class=HydJobsSerializer
    queryset=HydJobs.objects.all()

