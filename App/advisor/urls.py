from django.urls import path, include
from rest_framework.routers import DefaultRouter

from advisor import views 

router = DefaultRouter()
router.register('advisor', views.AdvisorViewSet)

app_name = 'advisor'

urlpatterns = [
    path('', include(router.urls)),
]