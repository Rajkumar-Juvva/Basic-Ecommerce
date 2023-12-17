from django.db import models

# Create your models here.
#cognoai
#1234
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

class Products(models.Model):
    TYPE_CHOICES = (
        ('home', 'Home'),
        ('work', 'Work'),
        ('mobile', 'Mobile'),
        ('other', 'Other'),
    )
    label = models.CharField(max_length=10, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='product_images')
    created_time = models.DateTimeField(auto_now_add= True)
    delete_flag = models.BooleanField(null=True,blank=True)
    class Meta:
        db_table = 'products_master_table'
        verbose_name = "My Model"
        verbose_name_plural = "Products to select"
    def __str__(self) -> str:
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add= True)
    delete_flag = models.BooleanField(null=True,blank=True)
    class Meta:
        db_table = 'user_cart_table'

class userRequestCountTrack(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    request_count = models.IntegerField(default=0)
class banned_users(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

