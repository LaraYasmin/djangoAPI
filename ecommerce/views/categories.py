from ..models.categories import Categorie
from ..serializers.categoriesSerializer import CategorieSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
class Categories(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            categories = Categorie.get_all_categories()
            serializer = CategorieSerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Error to get categories"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        category_name = request.data.get('category_name')
        category = Categorie.create_category(category_name=category_name)
        if category:
            serializer = CategorieSerializer(category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Error to create category"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        try:
            id = request.data.get('id')
            delete = Categorie.delete_category(id)
            return Response(delete, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"error": "Error to delete category"}, status=status.HTTP_404_NOT_FOUND)