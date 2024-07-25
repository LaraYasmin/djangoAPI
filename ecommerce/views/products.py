from ..models.products import Product
from ..serializers.productsSerializer import ProductSerializers
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import status

class Products(APIView):
    def get(self, request):
        ids = request.params.get('ids', None)
        if ids:
            products = Product.get_all_products_by_category_id(ids)
        products = Product.get_all_products()
        
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
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
    
    def delete(self, request):
        try:
            id = request.data.get('id')
            deleted_product = Product.delete_product(id)
            return Response(deleted_product, status=status.HTTP_204_NO_CONTENT) 
        except:
            return Response({"error": "Error to delete product"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request):
        product_name = request.data.get('product_name')
        value_product = request.data.get('value_product')
        image_product = request.Files.get('image_product')
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
            return Response(updated_product, status=status.HTTP_200_OK)
        return Response({"error": "Error to update product"}, status=status.HTTP_400_BAD_REQUEST)