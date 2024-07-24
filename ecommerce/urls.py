from django.urls import path
from .views.login import Login
# from .views.orders import Orders
# from .views.home import Home
# from .views.signup import Signup

urlpatterns = [
    # path('home/', home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('login/user/<int:user_id>/', Login.as_view(), name='login_user'),
    # path('register/', signup.as_view(), name='register'),
    # path('orders/', orders.as_view(), name='orders'),
    # path('orders/user/<int:user_id>/', orders.as_view(), name='orders_user'),
]