from django.urls import path 

from user import views 

app_name = 'user'

urlpatterns = [
    path('register/', views.CreateuserView.as_view(), name='register'),
]