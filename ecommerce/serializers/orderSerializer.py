from restFramerwork import serializers
from ..models.orders import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user_id', 'product_id', 'quantity', 'status']