from django.db import models

# Create your models here.
#cognoai
#1234
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

class Products2(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='product_images')
    created_time = models.DateTimeField(auto_now_add= True)
    delete_flag = models.BooleanField(null=True,blank=True)
    class Meta:
        db_table = 'products_master_table_2'
    def __str__(self) -> str:
        return self.name

class Cart2(models.Model):
    user = models.ManyToManyField(User)
    product_id = models.ForeignKey(Products2,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add= True)
    delete_flag = models.BooleanField(null=True,blank=True)
    class Meta:
        db_table = 'user_cart_table_2'

