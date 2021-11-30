from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from store.models import Restaurant

from store.models import *


@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.all().filter(user=request.user).count()

    total_oder = Order.objects.count()
    orders = Order.objects.all().order_by('-id')
    context = {
        'product': total_product,
        'order': total_oder,
        'orders': orders
    }
    return render(request, 'dashboard.html', context)


def homePage(requst):
    restaurant = Restaurant.objects.all().order_by('-id')[:3]
    context = {'restaurant': restaurant}
    return render(requst, 'home.html', context)
