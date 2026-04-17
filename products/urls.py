from django.urls import path
from .views import product_list, rate_product
urlpatterns = [
    path('api/products/', product_list, name='product-list'),
    path('api/products/<int:product_id>/rate/', rate_product, name='rate_product')
]
