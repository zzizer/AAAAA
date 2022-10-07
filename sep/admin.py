from django.contrib import admin
from .models import Product, Category, NewDebt, NewSale, ModeofPayment, Customer, Measured_in,Status


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(NewDebt)
admin.site.register(NewSale)
admin.site.register(ModeofPayment)
admin.site.register(Customer)
admin.site.register(Status)
admin.site.register(Measured_in)
