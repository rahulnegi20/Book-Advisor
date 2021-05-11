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
from rest_framework.decorators import api_view
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


class AdvisorListViewSet(ReadWriteSerializerMixin, generics.RetrieveUpdateAPIView, viewsets.ModelViewSet):
    """Lists the availabe advisors to the user"""
   # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Advisor.objects.all()
    #serializer_class = BookingSerializer 
    read_serializer_class = BookingSerializer
    write_serializer_class = AdvisorSerializer
    http_method_names = ['get', 'head', 'post']
    #lookup_field = 'bookingtime'
    # lookup_url_kwarg = 'pk'

    # def get_object(self):
    #     #email = self.kwargs['user'] 
    #     return get_object_or_404(Advisor.obje)

    # def update(self, request, *args, **kwargs):
    #     advisor = Advisor.objects.filter(pk=request)
    #     return advisor.update(bookingtime='2021-05-10T19:09:28.332931Z')

    # def get_queryset(self, **user_id):
    #     """Return objects for the current authenticated user only"""
    #     return self.queryset.order_by('id') 
    
    # def get_booking(self, request, data):
    #     data = request.DATA 
    #     id = self.request.user.id
    #     queryset = Advisor.objects.filter(pk=id)
    #     serializer = BookingSerializer(queryset, data=data, many=True, partial=True)
    #     serializer.save()
        

# class AdvisorViewSet(viewsets.ViewSet, generics.RetrieveUpdateAPIView):

#     permission_classes = (IsAuthenticated,)
#     queryset = Advisor.objects.all()
#     serializer_class = AdvisorSerializer 


#     def list(self, request):
#         queryset = Advisor.objects.all()
#         serializer = AdvisorSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Advisor.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = BookingSerializer(user)
#         return Response(serializer.data)





class BookingAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Advisor.objects.all()

    # def get_queryset(self, **pk):
    #     advisor_id = self.advisor.id
    #     return self.queryset.filter(pk=advisor_id)

    def perform_update(self, request, serializer):
        """save and post the data"""
        data = request.data
        serializer.save(user=self.request.user, data=data, many=True)