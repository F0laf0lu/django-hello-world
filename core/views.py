from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Report, Location
from .serializers import ReportSerializer, LocationSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all().order_by('-date_reported')
    serializer_class = ReportSerializer
    

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]
