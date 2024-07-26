from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=50)
    
    def register(self):
        return self.save()
    
    @staticmethod
    def check_user_by_email(email):
        try:
            return UserInfo.objects.get(email=email)
        except:
            return f"User not found"
        
    @staticmethod
    def list_all_users():
        return UserInfo.objects.all()

    def user_exists(self):
        if UserInfo.objects.filter(email=self.email):
            return True
        return False
    
    def __str__(self):
        return f"{self.name} ({self.email})"