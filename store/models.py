from django.db import models
from users.models import User


class Restaurant(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=225, unique=True)
    address = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=120, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=220, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, null=None)
    name = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    drink = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(default='default.png')

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )

    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, default=None, null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICE, default="processing")
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name


# class testUser(models.Model):
#     name = models.CharField(max_length=120)
#     email = models.EmailField()
#     password = models.CharField(max_length=120)
#     created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name
