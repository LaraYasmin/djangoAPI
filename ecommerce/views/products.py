from ..models.products import Product
from ..serializers.productsSerializer import ProductSerializers
from rest_framework.response import Response
from rest_framework.views import APIView 

class Products(APIView):
    def get(self, request):
        ids = request.params.get('ids', None)
        if ids:
            products = Product.get_all_products_by_category_id(ids)
        products = Product.get_all_products()
        
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)