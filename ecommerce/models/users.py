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