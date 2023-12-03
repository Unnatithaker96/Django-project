from django.db import models
import datetime
from .product import Product
from .user import CustomUser

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_by_user(user_id):
        return Order.objects.filter(user=user_id).order_by('-date')

    def __str__(self):
        return f"Order: {self.quantity} {self.product}, by {self.user}, price {self.price}, at {self.date}, status: {self.status}"
    
    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        
