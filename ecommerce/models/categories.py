from django.db import models

class Categorie(models.Model):
    category_name = models.CharField(max_length=50)
    
    @staticmethod
    def get_all_categories():
        return Categorie.objects.all()
    
    @staticmethod
    def create_category(category_name):
        return Categorie.objects.create(category_name=category_name)
    
    def delete_category(category_name):
        return Categorie.objects.filter(id=category_name).delete()
    
    def __str__(self):
        return self.category_name