from django.urls import path
from .views import PaymentCreateIntentView, PaymentListView

urlpatterns = [
    path('create-intent/', PaymentCreateIntentView.as_view(), name='payment-create-intent'),
    path('list/', PaymentListView.as_view(), name='payment-list'),
]
