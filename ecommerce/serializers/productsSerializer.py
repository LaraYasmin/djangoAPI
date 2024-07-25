from rest_framework import serializers
from ..models.products import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'value_product', 'image_product', 'description_product', 'category_id']