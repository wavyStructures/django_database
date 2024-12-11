from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=True)
    email_address = models.CharField(max_length=50, blank=True, default="")
    account = models.FloatField(blank=True, null=True)
    # one-to-many Order
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    # many-to-many Order
    
class Bill(models.Model):
    total_amount = models.FloatField()
    is_paid = models.BooleanField(default=False)
    pass