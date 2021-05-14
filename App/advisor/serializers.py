from rest_framework import serializers
from core.models import Advisor


class AdvisorSerializer(serializers.ModelSerializer):
    """Serializer for Advisor object"""

    class Meta:
        model = Advisor
        fields = ('id', 'name', 'image')
        read_only_fields = ('id',)
        lookup_field = 'pk'
        
        