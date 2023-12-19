# urls.py
from django.urls import path
from . import views
from django.contrib.auth  import views as auth_views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'assets/index.html'), name= 'logout'),
    path('signup/', views.signup_view, name='signup'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('home/', views.home_view, name='home'),
    # Dynamic URL for category-specific product list
    path('products/category/<str:category_name>/', views.product_list_category, name='product_list_category'),

    # Add more URLs as needed
]
