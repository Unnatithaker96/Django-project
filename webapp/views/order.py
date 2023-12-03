from django.shortcuts import render, redirect
#from django.contrib.auth.hashers import check_password
from webapp.models.user import CustomUser
from django.views import View
from webapp.models.product import Products
from webapp.models.orders import Order
#from webapp.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        user = request.session.get('user')
        orders = Order.get_orders_by_user(user)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})
