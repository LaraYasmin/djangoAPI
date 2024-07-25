from django.db import models

class Order(models.Model):
    user_id = models.ForeignKey("User", on_delete=models.CASCADE, default=1)
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField()
    status = models.BooleanField()
    
    def verify_order(self):
        if self.quantity <= 0:
            raise ValueError("Invalid quantity")
        if not self.product_id:
            raise ValueError("Invalid product")
        
    def save(self, *args, **kwargs):
        self.verify_order()
        super().save(*args, **kwargs)
        
    @staticmethod
    def get_all_orders():
        return Order.objects.all()
    
    @staticmethod
    def get_order_by_user(user_id):
        return Order.objects.filter(user=user_id).order_by('-date')
        
    def __str__(self):
        return f"{self.user_id} ({self.product_id})"