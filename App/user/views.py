from rest_framework import generics, mixins, permissions, \
                           viewsets, authentication, status
#from rest_framework.authtoken.views import ObtainAuthToken
#from rest_framework.settings import api_settings
#from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.views import APIView 
#from django.shortcuts import get_object_or_404

from advisor import serializers

from user.serializers import UserSerializer, AuthTokenSerializer, BookingSerializer, \
                                BookingListSerializer
from advisor.serializers import AdvisorSerializer

from core.models import Advisor, User, BookingTime

from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

#from django.core.exceptions import ValidationError


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

    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    http_method_names = ['get' ,'head']
    def get_queryset(self):
        id = self.request.user.id   
        queryset = User.objects.filter(pk=id)
        return queryset


class AdvisorListView( mixins.ListModelMixin, APIView):
    """Lists the availabe advisors to the user"""

    permission_classes = (IsAuthenticated,)
    queryset = Advisor.objects.all().order_by('id')
    serializer_class = AdvisorSerializer

    def get(self, request, pk):
        advisors = Advisor.objects.all()
        serializer = AdvisorSerializer(advisors, many=True)
        return Response(serializer.data)



class BookingAPI(APIView):
    """APIView to book an advisor"""

    permission_classes = (IsAuthenticated,)
    serializer_class = BookingSerializer

    queryset = BookingTime.objects.all()
    lookup_field = 'apk'
    lookup_url_kwarg = 'apk'
    http_method_names = ['post', 'get']

    def post(self, request, apk, *args, **kwargs):
  
        user = self.request.user 
        advisor = Advisor.objects.get(pk=apk)
        date_time_field = request.data['booking_time']

        instance = BookingTime.objects.create(advisor=advisor, user=user, booking_time=date_time_field)
        if instance is not None:
            instance.save()
            return Response(status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)    


class BookingListView(mixins.ListModelMixin, APIView):
    """Listing View for booked advisors"""
    permission_classes = (IsAuthenticated,)
    serializer_class = BookingListSerializer


    def get(self, request, **pk):
        queryset = BookingTime.objects.filter(user=self.request.user)
        serializer = BookingListSerializer(queryset , many=True)
        return Response(serializer.data)

