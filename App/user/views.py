from rest_framework import generics, mixins, permissions, \
                           viewsets, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

from django.shortcuts import get_object_or_404

from advisor import serializers

from user.serializers import UserSerializer, AuthTokenSerializer

from core.models import Advisor, User

from rest_framework.response import Response




class CreateuserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserViewSet(viewsets.ModelViewSet):
    """A simple viewset for listing an retrieving viewsets"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    http_method_names = ['get' ,'head']
    def get_queryset(self):
        id = self.request.user.id
        queryset = User.objects.filter(pk=id)
        return queryset


class AdvisorListViewSet(viewsets.ModelViewSet, mixins.ListModelMixin):
    """Lists the availabe advisors to the user"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Advisor.objects.filter()
    serializer_class = serializers.AdvisorSerializer
    #lookup_field = 'user_id'
    #lookup_url_kwarg = 'pk'


    def get_queryset(self, **user_id):
        """Return objects for the current authenticated user only"""
        return self.queryset.order_by('id')

