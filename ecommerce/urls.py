from django.urls import path
from .views.login import Login
from .views.orders import Order
from .views.signup import Signup
from .views.products import Products, ProductDetail
from .views.categories import Categories

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('login/user/<int:user_id>/', Login.as_view(), name='login_user'),
    path('register/', Signup.as_view(), name='register'),
    path('orders/', Order.as_view(), name='orders'),
    path('orders/user/<int:user_id>/', Order.as_view(), name='orders_user'),
    path('products/', Products.as_view(), name='products'),
    path('products/details/', ProductDetail.as_view(), name='product'),
    path('categories/', Categories.as_view(), name='categories'),
    path('categories/<int:category_id>/', Categories.as_view(), name='category'),
]