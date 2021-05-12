from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from advisor import views 
from . import views 

router = DefaultRouter()

router.register('advisor', views.AdvisorListViewSet)
#router.register('advisor', views.AdvisorViewSet)
router.register('', views.UserViewSet, basename='user')
router.register('booking', views.BookingListViewSet)
#router.register('', views.BookingAPIView)

app_name = 'user'


urlpatterns = [

    path('login/', views.LoginAPIView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.CreateuserView.as_view()),
    path('<int:userid>/', include(router.urls)),
    # path('<int:user_id>/advisor/<int:advisor_id>/', views.BookingAPIView.as_view()),
    #path('booking/', views.AdvisorDetial.as_view())
]

