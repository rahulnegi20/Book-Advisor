import os 
import uuid
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings


def advisor_image_file_path(instance, filename):
    """Generate file path for new advisor image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/advisor', filename)



class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and saves a new user"""
        if not email:
            raise ValueError('User must have an email address to register!')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password):
        """Creates a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user     


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Advisor(models.Model):
    """Advisor object to be booked"""
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=advisor_image_file_path)
    
    def __str__(self):
        return str(self.pk) 



class BookingTime(models.Model):
    """Booking the Advisor"""
    advisor = models.ForeignKey(
        Advisor,
        on_delete = models.CASCADE, null=False, blank=False
    )
    booking_time = models.DateTimeField(
                            auto_now_add=False,
                            auto_now=False,
                            unique=True
                            )
    user = models.ForeignKey(
                    User,
                    on_delete = models.CASCADE, null=False, blank=False
                    )
    
    def __str__(self):
        return "{}".format(self.date_time_field)