from ..models.orders import Order
from ..serializers.orderSerializer import OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class Order(APIView):
    def get(self, request):
        orders = Order.get_order_by_user(request.user_id)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        send_order = Order.sendOrder(request.data)
        serializer = OrderSerializer(send_order, many=False)
        return Response(serializer.data)