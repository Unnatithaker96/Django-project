from django.db import models

from django.urls import reverse #To create our custome url
# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=250, db_index=True) 
    #if the db_index is set to TRUE then we can retrive data faster and memory usage and query accelaration.
    slug = models.SlugField(max_length=250, unique=True)
    #Slug field used to maintain unique page for each category
    
    
    class Meta:
        
        verbose_name_plural = 'categories'
        
        
    def __str__(self):
        return self.name 
    
        #function to create our own url reverse
    def get_absolute_url(self):
        
       return  reverse('list-category', args=[self.slug])
    
    
class Product(models.Model):
    
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True) # is created to maintain the relation bw categories and products
    
    title = models.CharField(max_length=250)
    
    brand = models.CharField(max_length=250, default='un-branded')
    
    description = models.TextField(blank=True) 
    
    slug = models.SlugField(max_length=255)
    
    price = models.DecimalField(max_digits=4, decimal_places=2)
    
    image = models.ImageField(upload_to='images/')
    
    
    class Meta:
        
        verbose_name_plural = 'products'
        
        
    def __str__(self):
        return self.title 
    
    
    #function to create our own url reverse
    def get_absolute_url(self):
        
        return  reverse('product-info', args=[self.slug])
        
    