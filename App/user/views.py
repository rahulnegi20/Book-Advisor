from rest_framework import generics, mixins, permissions, \
                           viewsets, authentication, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.views import APIView 
from django.shortcuts import get_object_or_404

from advisor.serializers import AdvisorSerializer
from user.serializers import UserSerializer, AuthTokenSerializer, BookingSerializer

from core.models import Advisor, User, Booking

from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CreateuserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


# class CreateTokenView(ObtainAuthToken):
#     """Create a new auth token for user"""
#     serializer_class = AuthTokenSerializer
#     renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        #extra response
        data['user id'] = self.user.id 

        return data


class LoginAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    """A simple viewset for listing an retrieving viewsets"""
   # authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    http_method_names = ['get' ,'head']
    def get_queryset(self):
        id = self.request.user.id
        queryset = User.objects.filter(pk=id)
        return queryset


class AdvisorListViewSet(viewsets.ReadOnlyModelViewSet, mixins.ListModelMixin):
    """Lists the availabe advisors to the user"""
   # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer 
    http_method_names = ['get', 'head']
    #lookup_field = 'user_id'
    #lookup_url_kwarg = 'pk'


    def get_queryset(self, **user_id):
        """Return objects for the current authenticated user only"""
        return self.queryset.order_by('id') 

    def get_booking(self):
        pass


class BookingAPIView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Booking.objects.all()

    # def get_queryset(self, **pk):
    #     advisor_id = self.advisor.id
    #     return self.queryset.filter(pk=advisor_id)

    def perform_create(self, serializer):
        """save and post the data"""
        serializer.save(user=self.request.user)