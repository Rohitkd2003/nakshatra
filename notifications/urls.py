from django.urls import path
from .views import NotificationListView, SendNotificationView

urlpatterns = [
    path('list/', NotificationListView.as_view(), name='notification-list'),
    path('send/', SendNotificationView.as_view(), name='notification-send'),
]
