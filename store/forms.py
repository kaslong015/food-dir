from django import forms

from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'price'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'quantity'
            })
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-control', 'id': 'product'
            }),

        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

        widgets = {
            'order': forms.Select(attrs={
                'class': 'form-control', 'id': 'order'
            }),
            'courier_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'courier_name'
            }),
        }


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'drink', 'price', 'picture']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'drink': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'drink'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'price'
            }),

        }


class RestuarantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'image']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'address'
            }),

        }
