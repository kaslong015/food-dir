from django.urls import path

from .views import (
    create_restuarant,
    create_product,
    create_order,

    ProductListView,
    OrderListView,

    FoodListView,
    RestuarantListView,
    createFood,
    editRestDatails
)

urlpatterns = [


    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('food-list/', FoodListView, name='food-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('create-food/', createFood, name='create-food'),
    path('create-restuarant/', create_restuarant, name='create-restuarant'),
    path('restuarant-list/', RestuarantListView.as_view(), name='restuarant-list'),
    path('editrest/<str:pk>/', editRestDatails, name='editrest')
]
