from django.urls import path
from .views.store import store
from .views.cart import Cart
from .views.categories import categories, list_category
from .views.checkout import CheckOut
from .views.order import OrderView
from .views.product_info import product_info

from .middlewares.auth import  auth_middleware


urlpatterns = [
    #Store main page URL
    path('', store, name='store'),
    #Individual Prodcut
    path('product/<slug:product_slug>/', product_info, name='product-info'), #By using slug field we can get individual product view
    #individual Category
    path('search/<slug:category_slug>/', list_category, name='list-category'), #By using slug field we can get individual Catrgory view
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    ] 
