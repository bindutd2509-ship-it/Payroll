import razorpay
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment

# Create Payment
class CreatePayment(APIView):

    def post(self, request):
        employee_name = request.data.get("employee_name")
        amount_str = request.data.get("amount")

        if not employee_name:
            return Response({"error": "employee_name is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not amount_str or not str(amount_str).strip():
            return Response({"error": "amount is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            amount = int(float(amount_str))
            if amount <= 0:
                return Response({"error": "amount must be positive"}, status=status.HTTP_400_BAD_REQUEST)
        except (ValueError, TypeError):
            return Response({"error": "amount must be a valid positive number"}, status=status.HTTP_400_BAD_REQUEST)

        client = razorpay.Client(auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        ))

        order = client.order.create({
            "amount": amount * 100,
            "currency": "INR",
            "payment_capture": 1
        })

        payment = Payment.objects.create(
            employee_name=employee_name,
            amount=amount,
            razorpay_order_id=order["id"]
        )

        return Response({
            "order_id": order["id"],
            "amount": amount,
            "key": settings.RAZORPAY_KEY_ID
        })


# Verify Payment
class VerifyPayment(APIView):

    def post(self, request):

        client = razorpay.Client(
            auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
        )

        params_dict = {
            "razorpay_order_id": request.data.get("razorpay_order_id"),
            "razorpay_payment_id": request.data.get("razorpay_payment_id"),
            "razorpay_signature": request.data.get("razorpay_signature")
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            return Response({"message": "Payment verified successfully"})
        except:
            return Response({"message": "Payment verification failed"})
