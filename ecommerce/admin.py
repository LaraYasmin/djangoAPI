from django.contrib import admin

# Register your models here.
from .models.orders import Order
from .models.categories import Categorie
from .models.products import Product
from .models.users import UserInfo

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(Order)