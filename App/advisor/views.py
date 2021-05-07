from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Advisor

from advisor import serializers


class AdvisorViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin):
    """Manage Advisor in the database"""
    queryset = Advisor.objects.all()
    serializer_class = serializers.AdvisorSerializer

    def get_queryset(self):
        """Return objects"""
        return self.queryset.filter().order_by('-name')

    def perform_create(self, serializer):
        """Create a new Advisor"""
        serializer.save()
