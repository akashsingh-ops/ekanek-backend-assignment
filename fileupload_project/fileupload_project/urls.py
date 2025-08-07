from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import PublicFileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # <-- mounts /api/login/
    path('public/<str:short_url>/', PublicFileView.as_view(), name='public-file')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
