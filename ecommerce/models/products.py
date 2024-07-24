from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    value_product = models.DecimalField(max_digits=10, decimal_places=2)
    image_product = models.ImageField(upload_to='uploads/products/')
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
    
    def __str__(self):
        return f"{self.product_name} ({self.value_product})"