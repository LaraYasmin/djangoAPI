from ..models.categories import Categorie
from ..serializers.categoriesSerializer import CategorieSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class Categories(APIView):
    def get(self, request):
        categories = Categorie.get_all_categories()
        serializer = CategorieSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)