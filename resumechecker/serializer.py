from rest_framework import serializers
from .models import Jobs,Resume

class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Jobs
        fields='__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resume
        fields='__all__'
