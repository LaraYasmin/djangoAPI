from ..models.products import Product
from ..serializers.productsSerializer import ProductSerializers
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.permissions import AllowAny

class Products(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        ids = request.query_params.get('ids', None)
        if ids:
            products = Product.get_all_products_by_category_id(ids)
        products = Product.get_all_products()
        
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductDetail(APIView):
    def post(self, request):
        product_name = request.data.get('product_name')
        value_product = request.data.get('value_product')
        image_product = request.FILES.get('image_product') 
        description_product = request.data.get('description_product')
        category_id = request.data.get('category_id')
        
        new_product = Product.post_new_product(
            product_name=product_name,
            value_product=value_product,
            image_product=image_product,
            description_product=description_product,
            category_id=category_id
        )
        
        if new_product:
            serializer = ProductSerializers(new_product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Fill all the fields"}, status=status.HTTP_400_BAD_REQUEST)
        
class ProductUpdate(APIView):
    def put(self, request, id):
        product_name = request.data.get('product_name')
        value_product = request.data.get('value_product')
        image_product = request.FILES.get('image_product')
        description_product = request.data.get('description_product')
        category_id = request.data.get('category_id')
        
        if all([product_name, value_product, image_product, description_product, category_id]):
            updated_product = Product.update_product(
                product_id=id,
                product_name=product_name,
                value_product=value_product,
                image_product=image_product,
                description_product=description_product,
                category_id=category_id
            )
            
            serializer = ProductSerializers(updated_product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Error to update product"}, status=status.HTTP_400_BAD_REQUEST)

class ProductDelete(APIView):
    def delete(self, request, id):
        try:
            Product.delete_product(id)
            return Response(status=status.HTTP_204_NO_CONTENT) 
        except Product.DoesNotExist:
            return Response({"error": "Error to delete product"}, status=status.HTTP_404_NOT_FOUND)
