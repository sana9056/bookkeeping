from rest_framework.serializers import ModelSerializer
from .models import Staff


class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
