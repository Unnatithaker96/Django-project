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
