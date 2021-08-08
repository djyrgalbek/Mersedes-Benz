from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('add-product/', ProductCreateView.as_view(), name='add-product'),
    path('update-product/<int:pk>/', ProductUpdateView.as_view(), name='update-product'),
    path('delete-product/<int:pk>/', DeleteProductView.as_view(), name='delete-product'),
    path('filter-product/', FilterPageView.as_view(), name='filter-product'),
    path('search/', SearchPageView.as_view(), name='search'),

    # cart urls
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
]