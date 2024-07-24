from restFramerwork import serializers
from ..models.categories import Categorie

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'category_name']