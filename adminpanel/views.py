from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import AdminUserSerializer

User = get_user_model()

class AdminUserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [permissions.IsAdminUser]  # फक्त admin वापरकर्ता

class AdminUserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_url_kwarg = 'user_id'
