from django.db import models

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