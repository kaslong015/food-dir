from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    Product,
    Order,
    Delivery,
    Food,
    Restaurant
)
from .forms import (
    ProductForm,
    OrderForm,
    DeliveryForm,
    FoodForm,
    RestuarantForm
)


def createFood(request):
    forms = FoodForm()
    context = {}
    if request.method == 'POST':
        forms = FoodForm(request.POST)
        if forms.is_valid():
            Job = forms.save(commit=False)
            # print(request.user)
            print(type(Restaurant.objects.all()))
                # print(i.name)

            # print(Job.restaurant)
            # Job.save()

    context = {'form': forms}
    return render(request, 'store/createfood.html', context)


# Product views
@ login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            # print(forms.cleaned_data)
            instance = forms.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product'


class FoodListView(ListView):
    model = Food
    template_name = 'store/food_list.html'
    context_object_name = 'product'

# Order views


@ login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_order.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'store/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all().order_by('-id')
        return context


# Delivery views
@ login_required(login_url='login')
def create_delivery(request):
    forms = DeliveryForm()
    if request.method == 'POST':
        forms = DeliveryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('delivery-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_delivery.html', context)


@ login_required(login_url='login')
def create_restuarant(request):
    forms = RestuarantForm()
    context = {}

    if request.method == "POST":
        forms = RestuarantForm(request.POST)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('restuarant-list')

    context = {"form": forms}
    return render(request, 'store/create_restuarant.html', context)


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'store/delivery_list.html'
    context_object_name = 'delivery'


class RestuarantListView(ListView):
    model = Restaurant
    template_name = 'store/restuarant_list.html'
    context_object_name = 'restuarant'
