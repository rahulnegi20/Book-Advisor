from django.urls import path, include 

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from advisor import views 
from . import views 


app_name = 'user'


urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.CreateuserView.as_view()),
    path('<int:pk>/advisor', views.AdvisorListView.as_view()),
    path('<int:pk>/advisor/<int:apk>/', views.BookingAPI.as_view()),
    path('<int:pk>/advisor/booking/', views.BookingListView.as_view())
]
