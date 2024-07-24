import email
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=50)
    
    def register(self):
        return self.save()
    
    @staticmethod
    def get_user_by_email():
        try:
            return User.objects.get(email=email)
        except:
            return f"User not found"

    def if_user_exists(self):
        if User.objects.filter(email=self.email):
            return True
        return False
    
    def __str__(self):
        return f"{self.name} ({self.email})"

class Categorie(models.Model):
    category_name = models.CharField(max_length=50)
    
    @staticmethod
    def get_all_categories():
        return Categorie.objects.all()
    
    def __str__(self):
        return self.category_name
    
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

class Order(models.Model):
    user_id = models.ForeignKey("User", on_delete=models.CASCADE, default=1)
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField()
    status = models.BooleanField()
    
    def sendOrder(self):
        return self.save()
    
    @staticmethod
    def get_order_by_user(user_id):
        return Order.objects.filter(user=user_id).order_by('-date')
    
    @staticmethod
    def get_all_orders():
        return Order.objects.all()
        
    def __str__(self):
        return f"{self.user_id} ({self.product_id})"