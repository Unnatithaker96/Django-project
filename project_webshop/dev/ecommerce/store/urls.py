from django.urls import path

from . import views

urlpatterns = [
    
    #Store main page URL
    
    path('', views.store, name='store'),
    
    
    #Individual Prodcut
    
    path('product/<slug:product_slug>/', views.product_info, name='product-info'), #By using slug field we can get individual product view
    
    #individual Category
    
    path('search/<slug:category_slug>/', views.list_category, name='list-category'), #By using slug field we can get individual Catrgory view
]
