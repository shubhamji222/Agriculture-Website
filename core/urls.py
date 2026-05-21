from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sales/', views.sales_page, name='sales'),
    path('purchase/', views.purchase_page, name='purchase'),
    path('dispatch/', views.dispatch_page, name='dispatch'),
    path('farmers/', views.farmers_page, name='farmers'),
    path('procurement/', views.procurement_page, name='procurement'),
    path('payments/', views.payments_page, name='payments'),
]
