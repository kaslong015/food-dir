from django.urls import path

from .views import (
    create_restuarant,
    create_product,
    create_order,
    create_delivery,

    ProductListView,
    OrderListView,
    DeliveryListView,
    FoodListView,
    RestuarantListView,
    createFood
)

urlpatterns = [


    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('food-list/', FoodListView.as_view(), name='food-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
    path('create-food/', createFood, name='create-food'),
    path('create-restuarant/', create_restuarant, name='create-restuarant'),
    path('restuarant-list/', RestuarantListView.as_view(), name='restuarant-list'),
]
