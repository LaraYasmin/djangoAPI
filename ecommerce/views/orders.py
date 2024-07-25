from ..models.orders import Order
from ..serializers.orderSerializer import OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny

class Order_User(APIView):
    def get(self, request, user_id):
        try:
            orders = Order.get_order_by_user(user_id)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Error to get user orders"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response({"error": "Error to send order"}, status=status.HTTP_400_BAD_REQUEST)

class OrderAll(APIView):
        def get(self, request):
            try:
                orders = Order.get_all_orders()
                serializer = OrderSerializer(orders, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                raise Response({"error": "Error to get orders"}, status=status.HTTP_404_NOT_FOUND)