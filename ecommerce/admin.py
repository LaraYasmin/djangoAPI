from django.contrib import admin

# Register your models here.
from .models.orders import Order
from .models.categories import Categorie
from .models.products import Product
from .models.users import User

# Register your models here.
admin.site.register(User)
admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(Order)