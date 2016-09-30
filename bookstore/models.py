#utf-8
from django.db import models

# Create your models here.
class Bookstore (models.Model):
    Book_id = models.CharField(max_length=20, default='no')
    ISBN = models.CharField(max_length=20, default='no')
    Book_name = models.CharField(max_length=20, default='no')
    Price = models.CharField(max_length=20, default='no')
    Author= models.CharField(max_length=20, default='no')