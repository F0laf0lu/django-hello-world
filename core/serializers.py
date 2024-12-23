from rest_framework import serializers
from .models import Report, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']

class ReportSerializer(serializers.ModelSerializer):
    location = serializers.CharField()
    location_name = serializers.ReadOnlyField(source='location.name')
    reporter_name = serializers.ReadOnlyField(source='reporter.username')

    class Meta:
        model = Report
        fields = [
            'id', 'title', 'description', 'location', 'location_name',
            'date_reported', 'status', 'reporter', 'reporter_name',
            'phone_number', 'image'
        ]
    
    def create(self, validated_data):
        location_name =  validated_data['location']
        location, created = Location.objects.get_or_create(name=location_name)
        validated_data['location'] = location
        return super().create(validated_data)