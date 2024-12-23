from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Report, Location
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ReportSerializer, LocationSerializer


class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]


class ReportViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Report.objects.all().order_by('-date_reported')
    serializer_class = ReportSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

