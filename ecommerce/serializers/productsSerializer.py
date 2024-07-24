from restFramerwork import serializers
from ..models.products import Product

class ProductSerializers(serializers.ModeSerializer):
    class Meta:
        model = Product
        field = ['id', 'product_name', 'value_product', 'image_product', 'description_product', 'category_id']