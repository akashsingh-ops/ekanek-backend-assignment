from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from django.utils.crypto import get_random_string

from django.http import FileResponse, Http404
from django.views import View

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id
        })
class FileViewSet(viewsets.ModelViewSet):
    serializer_class = UploadedFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return UploadedFile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        short_url = get_random_string(8)
        serializer.save(user=self.request.user, short_url=short_url)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def share(self, request, pk=None):
        file = self.get_object()
        return Response({"shareable_url": f"/public/{file.short_url}"})



class PublicFileView(View):
    def get(self, request, short_url):
        try:
            file = UploadedFile.objects.get(short_url=short_url)
            return FileResponse(file.file, as_attachment=True)
        except UploadedFile.DoesNotExist:
            raise Http404()