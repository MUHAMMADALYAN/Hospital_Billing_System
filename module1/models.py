from django.db import models

# Create your models here.


class Sale(models.Model):
    medicine_name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

class Client(models.Model):
    name=models.CharField(max_length=200)
    Adress= models.CharField(max_length=200)
    Phone=models.PositiveIntegerField()
    Email= models.CharField(max_length=200)

class Item(models.Model):
    party = models.CharField(max_length=200)
    Item=models.CharField(max_length=200)
    Rate=models.PositiveIntegerField()
    Medicine_Packets=models.PositiveIntegerField()
    Tax_Name = models.CharField(max_length=200)
    Tax_Rate = models.PositiveIntegerField()

