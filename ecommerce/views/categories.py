from ..models.categories import Categorie
from ..serializers.categoriesSerializer import CategorieSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class Categories(APIView):
    def get(self, request):
        categories = Categorie.get_all_categories()
        serializer = CategorieSerializer(categories, many=True)
        return Response(serializer.data)