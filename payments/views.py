from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import stripe
from django.conf import settings

# Set your Stripe secret key
stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentCreateIntentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["amount"],
            properties={
                "amount": openapi.Schema(type=openapi.TYPE_INTEGER, description="Amount in smallest currency unit"),
                "currency": openapi.Schema(type=openapi.TYPE_STRING, description="Currency code (default INR)"),
                "description": openapi.Schema(type=openapi.TYPE_STRING, description="Payment description"),
            },
        )
    )
    def post(self, request):
        try:
            amount = request.data.get("amount")  # integer, e.g., 5000 for 50.00
            currency = request.data.get("currency", "INR")
            description = request.data.get("description", "Payment")

            if not amount:
                return Response({"error": "Amount is required"}, status=status.HTTP_400_BAD_REQUEST)

            # Create Stripe PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=int(amount),
                currency=currency,
                description=description,
            )

            return Response(
                {
                    "client_secret": intent.client_secret,
                    "id": intent.id,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PaymentListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Temporary: return empty list or implement DB model later
        return Response({"payments": []}, status=status.HTTP_200_OK)
