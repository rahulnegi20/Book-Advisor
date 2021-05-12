from rest_framework import generics, mixins, permissions, \
                           viewsets, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.views import APIView 

from advisor.serializers import AdvisorSerializer
from user.serializers import UserSerializer, AuthTokenSerializer, BookingSerializer

from core.models import Advisor, User, Booking

from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .mixins import ReadWriteSerializerMixin


class CreateuserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


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


class AdvisorListViewSet(ReadWriteSerializerMixin, generics.UpdateAPIView, viewsets.ModelViewSet):
    """Lists the availabe advisors to the user"""
   # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Advisor.objects.all()
    #serializer_class = AdvisorSerializer 
    write_serializer_class = AdvisorSerializer
    read_serializer_class = BookingSerializer
    
    http_method_names = ['get', 'head', 'post','put']
    #lookup_field = 'pk'
   # lookup_url_kwarg = 'advisor_id'



class BookingListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Advisor.objects.all()

    def get_object(self):
        id = self.request.user.id
        queryset = Advisor.objects.filter(pk=id)
        return queryset