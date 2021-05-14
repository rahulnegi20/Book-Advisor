from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers 

from core.models import BookingTime

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object/Register"""

    class Meta:
        model = get_user_model()
        fields = ('id','name','email', 'password')
        extra_kwargs = {'password': {'write_only':True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """"Serializer for the user authentication object/Login"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credential')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user 
        return attrs     


class BookingSerializer(serializers.ModelSerializer):
    """Serialize Booking"""

    class Meta:
        model = BookingTime
        fields = ('id', 'booking_time',)
        read_only_fields=('id',)


class BookingListSerializer(serializers.ModelSerializer):
    """List of Booked Advisor(s)"""
    class Meta:
        model = BookingTime
        fields = ('advisor', 'booking_time', 'id',)
        read_only_fields = ('id',)
        depth = 1