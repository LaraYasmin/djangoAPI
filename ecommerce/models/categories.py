from django.db import models
from django.shortcuts import get_object_or_404

class Categorie(models.Model):
    category_name = models.CharField(max_length=50)
    
    @staticmethod
    def get_all_categories():
        return Categorie.objects.all()
    
    @staticmethod
    def create_category(category_name):
        return Categorie.objects.create(category_name=category_name)
    
    def delete_category(category_id):
        categorie = get_object_or_404(Categorie, id=category_id)
        categorie.delete()
        
        return categorie
    def __str__(self):
        return self.category_name