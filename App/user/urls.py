from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from advisor import views 
from . import views 

router = DefaultRouter()

router.register('advisor', views.AdvisorListViewSet)
router.register('', views.UserViewSet, basename='user')


app_name = 'user'


urlpatterns = [

    path('login/', views.LoginAPIView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.CreateuserView.as_view()),
    path('<int:user_id>/', include(router.urls)),
    path('booking', views.BookingAPI.as_view())
]

