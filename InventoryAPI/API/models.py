from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()

class Client(models.Model):
    service_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    contract_value = models.IntegerField()