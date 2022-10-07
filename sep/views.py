from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.http import HttpResponseRedirect
from .forms import NewsaleForm, AddDebtForm, AddProductForm, AddCustomerForm, ModeofPaymentForm, CategoryForm

def adminPannel(request):
    if 'searching' in request.GET:
        searched = request.GET['searching']
        #products = Product.objects.filter(name__icontains=searched)
        multipe_q = Q(Q(name__icontains=searched))
        products = Product.objects.filter(multipe_q)
    else:
        products = Product.objects.all()    
    
    context = {
        'products':products,
    }
    return render(request, 'seps_temp/admin.html', context)

def makesale(request):
    submitted = False
    
    if request.method =='POST':
        sales = NewsaleForm(request.POST)
        if sales.is_valid():
            sales.save()
            return HttpResponseRedirect('/make_sale?submitted=True')
    else:
        sales = NewsaleForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'sales':sales,
        'submitted':submitted,
    }
    return render(request, 'seps_temp/selling.html', context)

def makedebt(request):
    submitted = False
    
    if request.method =='POST':
        debts = AddDebtForm(request.POST)
        if debts.is_valid():
            debts.save()
            return HttpResponseRedirect('/make_debt?submitted=True')
    else:
        debts = AddDebtForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'debts':debts,
        'submitted':submitted,
    }
    return render(request, 'seps_temp/sellingondebt.html', context)

def addCustomer(request):
    submitted = False
    
    if request.method =='POST':
        customers = AddCustomerForm(request.POST)
        if customers.is_valid():
            customers.save()
            return HttpResponseRedirect('/add_Customer?submitted=True')
    else:
        customers = AddCustomerForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'customers':customers,
        'submitted':submitted,
    }
    return render(request, 'seps_temp/addcustomer.html', context)

def addProduct(request):
    submitted = False
    
    if request.method =='POST':
        products = AddProductForm(request.POST)
        if products.is_valid():
            products.save()
            return HttpResponseRedirect('/add_product?submitted=True')
    else:
        products = AddProductForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'products':products,
        'submitted':submitted,
    }
    return render(request, 'seps_temp/addproduct.html', context)

def viewCustomers(request):
    customers = Customer.objects.all()
    
    context = {
        'customers': customers,
    }
    return render(request, 'seps_temp/allcustomers.html', context)

def viewDebts(request):
    debts = NewDebt.objects.all()
    
    context = {
        'debts': debts,
    }
    return render(request, 'seps_temp/alldebts.html', context)

def updateCustomer(request,pk):
    customers = Customer.objects.get(id=pk)    
    form = AddCustomerForm(instance=customers)
    
    if request.method == 'POST':
        form = AddCustomerForm(request.POST,request.FILES, instance=customers)
        if form.is_valid():
            form.save()
            return redirect('view-customer')
        
    context = {'customers':form}
    return render(request, 'seps_temp/addcustomer.html', context)

def updateDebt(request, pk):
    debt = NewDebt.objects.get(id=pk)    
    form = AddDebtForm(instance=debt)
    
    if request.method == 'POST':
        form = AddDebtForm(request.POST,request.FILES, instance=debt)
        if form.is_valid():
            form.save()
            return redirect('view-debts')
        
    context = {'debts':form}
    return render(request, 'seps_temp/sellingondebt.html', context)

def customerDetails(request, pk):
    
    customer = Customer.objects.get(id=pk)
    
    context = {
        'customer':customer,
    }
    
    return render(request, 'seps_temp/singleCutomer.html', context)

def singlecustomerDebt(request, pk):
    
    debt = NewDebt.objects.get(id=pk)
    
    context = {
        'debt':debt,
    }
    
    return render(request, 'seps_temp/singlecustomerdebt.html', context)

