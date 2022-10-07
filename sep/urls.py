from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminPannel, name='adminPannel'),
    path('make_sale/', views.makesale, name='make_sale'),
    path('make_debt/', views.makedebt, name='make_debt'),
    path('add_Customer/', views.addCustomer, name='add_Customer'),
    path('add_product/', views.addProduct, name='add_product'),
    path('view-customer/', views.viewCustomers, name='view-customer'),
    path('view-debts/', views.viewDebts, name='view-debts'),           
    path('update-customer/<str:pk>/', views.updateCustomer, name='update-customer'),
    path('update-debt/<str:pk>/', views.updateDebt, name='update-debt'),
    path('customer-Details/<str:pk>', views.customerDetails, name='customer-Details'),
    path('single-customerDebt/<str:pk>', views.singlecustomerDebt, name='single-customerDebt'),      
]
