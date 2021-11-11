from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('signup/', signup_page, name='signup'),
]
