from django import forms

from .models import *


# class SupplierForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'name',
#         'data-val': 'true',
#         'data-val-required': 'Please enter name',
#     }))
#     address = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'address',
#         'data-val': 'true',
#         'data-val-required': 'Please enter address',
#     }))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#         'id': 'email',
#         'data-val': 'true',
#         'data-val-required': 'Please enter email',
#     }))
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'username',
#         'data-val': 'true',
#         'data-val-required': 'Please enter username',
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter password',
#     }))
#     retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'retype_password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter retype_password',
#     }))


# class BuyerForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'name',
#         'data-val': 'true',
#         'data-val-required': 'Please enter name',
#     }))
#     address = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'address',
#         'data-val': 'true',
#         'data-val-required': 'Please enter address',
#     }))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#         'id': 'email',
#         'data-val': 'true',
#         'data-val-required': 'Please enter email',
#     }))
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'username',
#         'data-val': 'true',
#         'data-val-required': 'Please enter username',
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter password',
#     }))
#     retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'retype_password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter retype_password',
#     }))


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
            # 'restaurant:': forms.Select(attrs={
            #     'class': 'form-control', 'id': 'restaurant'
            # }),
        }


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'drink', 'price', ]

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
            # 'restaurant:': forms.Select(attrs={
            #     'class': 'form-control', 'id': 'restaurant'
            # }),
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
            'picture': forms.FileInput(attrs={
                'class': 'form-control', 'id': 'picture'
            }),
        }


class RestuarantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'address'
            }),

        }
