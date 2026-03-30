"""
URL configuration for cattle_project project.
"""

from django.contrib import admin
from django.urls import path, include

# ✅ For media (image) handling
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cattle_app.urls')),   # app connected
]

# ✅ Serve uploaded images (VERY IMPORTANT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)