from django.urls import path, include 
from rest_framework.routers import DefaultRouter

from advisor import views 
from user import views 
from . import views 

router = DefaultRouter()

router.register('advisor', views.AdvisorListViewSet)
router.register('', views.UserViewSet, basename='user')


app_name = 'user'


urlpatterns = [
    path('register/', views.CreateuserView.as_view(), name='register'),
    path('login/', views.CreateTokenView.as_view(), name='token'),
    path('<int:user_id>/', include(router.urls)),
 
]

