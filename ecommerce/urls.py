from django.urls import path
from .views.login import Login
from .views.orders import Order_User, OrderAll
from .views.signup import Signup
from .views.products import Products, ProductDetail, ProductUpdate, ProductDelete
from .views.categories import Categories, CategoriesDelete, CategoriesPost
from .views.users import UsersInfoData

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Signup.as_view(), name='register'),
    path('users/', UsersInfoData.as_view(), name='users'),
    path('orders/<int:user_id>/', Order_User.as_view(), name='orders'),
    path('orders/all/', OrderAll.as_view(), name='orders_user'),
    path('products/list/', Products.as_view(), name='products'),
    path('products/create/', ProductDetail.as_view(), name='product'),
    path('products/update/<int:id>/',ProductUpdate.as_view(), name='product_update'),
    path('products/delete/<int:id>/', ProductDelete.as_view(), name='product_delete'),
    path('categories/', Categories.as_view(), name='categories'),
    path('categories/<int:id>/', CategoriesDelete.as_view(), name='categories_delete'),
    path('categories/create/', CategoriesPost.as_view(), name='categories'),
]