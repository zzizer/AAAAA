from django.db import models
from django.contrib.auth.models import User

#Sales Section
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Measured_in(models.Model):
    name = models.CharField(max_length=100, null=True)
    
    class Meta:
        verbose_name_plural = 'Measured In '
    
    def __str__(self):
        return self.name
    
class Status(models.Model):
    isAvailable =models.CharField(max_length=50, null=True)
    
    class Meta:
        verbose_name_plural = 'Status Of Product'
        
    def __str__(self):
        return self.isAvailable
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    unitPrice = models.FloatField()
    stocked = models.IntegerField()
    measuredin = models.ForeignKey(Measured_in, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.name} under {self.category}'
    
class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    accountBalance = models.FloatField()
    telnumber = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, null=True)
    address = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f'{self.name}---{self.accountBalance}'
    


class ModeofPayment(models.Model):
    mode =models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Mode of Payment'    
        
    def __str__(self):
        return self.mode
    
    
class NewSale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    modeofpayment = models.ForeignKey(ModeofPayment, on_delete=models.CASCADE, null=True)
    initiatedby = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Sales'
    
    def __str__(self):
        return f'{self.customer} bought {self.product} initiated by {self.initiatedby}'
    
    
class NewDebt(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    initiatedby = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    date = models.DateField(auto_now=False, null=True)
    
    class Meta:
        verbose_name_plural = 'Debts'
    
    def __str__(self):
        return f'{self.customer} took debt initiated by {self.initiatedby}'
    
    
    @property
    def total(self):
        totalprice = self.product.unitPrice * self.quantity
        return totalprice
    