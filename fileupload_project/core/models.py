from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import os
import mimetypes

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    mime_type = models.CharField(max_length=100, blank=True)
    short_url = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.mime_type:
            mime, _ = mimetypes.guess_type(self.file.name)
            self.mime_type = mime or 'application/octet-stream'
        super().save(*args, **kwargs)
