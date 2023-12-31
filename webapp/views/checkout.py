from django.shortcuts import render, redirect

#from django.contrib.auth.hashers import check_password
from webapp.models.customer import User
from django.views import View

from webapp.models.product import Product
from webbapp.models.orders import Order

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        user = request.session.get('user')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, user, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(user=User(id=user),
                          product=product,
                          price=product.price,
                          address=address,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')
