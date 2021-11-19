from rest_framework import serializers
from .models import Project, Measurement

class Projectserializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class Measurementserializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
