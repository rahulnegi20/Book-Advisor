from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings 



urlpatterns = [
    path('admins/', admin.site.urls),
    path('user/', include('user.urls')),
    path('admin/', include('advisor.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
