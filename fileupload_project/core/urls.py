from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import FileViewSet, CustomAuthToken

router = DefaultRouter()
router.register(r'files', FileViewSet, basename='files')

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),  # <-- login endpoint
    path('', include(router.urls)),
]
