from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    Product,
    Order,

    Food,
    Restaurant
)
from .forms import (
    ProductForm,
    OrderForm,

    FoodForm,
    RestuarantForm
)


def createFood(request):
    forms = FoodForm()
    context = {}
    if request.method == 'POST':
        forms = FoodForm(request.POST, request.FILES)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('food-list')

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


def FoodListView(request):
    products = Food.objects.filter(user=request.user)
    rest = Restaurant.objects.get(user=request.user)
    context = {'products': products, 'restaurant': rest.name}
    return render(request, 'store/food_list.html', context)


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


@ login_required(login_url='login')
def create_restuarant(request):
    forms = RestuarantForm()
    print(request.POST)
    if request.method == "POST":
        forms = RestuarantForm(request.POST, request.FILES)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('restuarant-list')

    context = {"form": forms}
    return render(request, 'store/create_restuarant.html', context)


class RestuarantListView(ListView):
    model = Restaurant
    template_name = 'store/restuarant_list.html'
    context_object_name = 'restuarant'

    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user)


def editRestDatails(request, pk):
    record = Restaurant.objects.get(id=pk)
    form = RestuarantForm(instance=record)

    if request.method == "POST":
        form = RestuarantForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'successful')
            return redirect('restuarant-list')

    context = {'form': form}
    return render(request, 'store/update_rest.html', context)
