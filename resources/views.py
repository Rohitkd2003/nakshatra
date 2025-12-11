from rest_framework import generics, permissions
from .models import Resource
from .serializers import ResourceSerializer

class ResourceCreateView(generics.CreateAPIView):
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ResourceListView(generics.ListAPIView):
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Resource.objects.all()
