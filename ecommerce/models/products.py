from django.db import models
from django.core.exceptions import ValidationError
from ecommerce.models.categories import Categorie
from django.shortcuts import get_object_or_404

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    value_product = models.DecimalField(max_digits=10, decimal_places=2)
    image_product = models.ImageField(upload_to='products/details/')
    description_product = models.TextField(max_length=255, default='', blank=False)
    category_id = models.ForeignKey("Categorie", on_delete=models.CASCADE, default=1)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        return Product.get_all_products()
    
    @staticmethod
    def post_new_product(product_name, value_product, image_product, description_product, category_id):
        if all([product_name, value_product, image_product, description_product, category_id]):
            try:
                category_id = Categorie.objects.get(id=category_id)
            except Categorie.DoesNotExist:
                raise ValidationError("Category does not exist")
            
            return Product.objects.create(
                product_name=product_name, 
                value_product=value_product, 
                image_product=image_product, 
                description_product=description_product, 
                category_id=category_id
            )
        raise ValidationError("Fill all the fields")
    
    @staticmethod
    def delete_product(product_id):
        product = get_object_or_404(Product, id=product_id)
        
        product.delete()
        return product
    
    @staticmethod
    def update_product(product_id, product_name, value_product, image_product, description_product, category_id):
        product = get_object_or_404(Product, id=product_id)
        category_instance = get_object_or_404(Categorie, id=category_id)

        product.product_name = product_name
        product.value_product = value_product
        product.image_product = image_product
        product.description_product = description_product
        product.category_id = category_instance
        
        product.save()
        return product
    
    def __str__(self):
        return f"{self.product_name} ({self.value_product})"