from django import forms
from django.forms import ModelForm
from .models import NewSale,Product, NewDebt, Customer, Category, ModeofPayment


class NewsaleForm(ModelForm):
    class Meta:
        model = NewSale
        fields = "__all__"
        
class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        
class AddDebtForm(ModelForm):
    class Meta:
        model = NewDebt
        fields = "__all__"

class ModeofPaymentForm(ModelForm):
    class Meta:
        model = ModeofPayment
        fields = "__all__"

class AddCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        