from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('service_requests.urls')),  # Include the service_requests URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
    path('accounts/logout/', LogoutView.as_view(), name='logout'),  # Explicitly define logout
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
