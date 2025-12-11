from django.urls import path
from .views import AdminUserListView, AdminUserDeleteView

urlpatterns = [
    path('admin/users/', AdminUserListView.as_view(), name='admin-user-list'),
    path('admin/users/<int:user_id>/delete/', AdminUserDeleteView.as_view(), name='admin-user-delete'),
]
