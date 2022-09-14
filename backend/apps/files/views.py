from rest_framework import viewsets

from core.permissions import IsSubscriber
from .models import File
from .serializers import FileSerializer



class FileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsSubscriber]
