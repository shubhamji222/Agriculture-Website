import django
from django.db.models import Sum
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework import request, viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
 
from .models import Federation, Farmer, FarmerPayment, Procurement, Purchase, Sale, Dispatch
from .serializers import (
    FederationSerializer,
    FarmerSerializer,
    FarmerPaymentSerializer,
    ProcurementSerializer,
    PurchaseSerializer,
    SaleSerializer,
    DispatchSerializer,
)


def dashboard(request):
    sales_total = Sale.objects.aggregate(total=Sum('amount'))['total'] or 0
    purchase_total = Purchase.objects.aggregate(total=Sum('cost'))['total'] or 0
    dispatch_pending = Dispatch.objects.filter(status__icontains='pending').count()
    procurement_qty = Procurement.objects.aggregate(total=Sum('quantity'))['total'] or 0
    farmer_count = Farmer.objects.count()

    latest_sales = Sale.objects.order_by('-date')[:3]
    latest_purchases = Purchase.objects.order_by('-date')[:3]
    latest_dispatches = Dispatch.objects.order_by('-date')[:3]

    latest_activity = []
    for sale in latest_sales:
        latest_activity.append({
            'date': sale.date,
            'type': 'Sales',
            'reference': sale.order_id,
            'amount': sale.amount,
            'status': sale.status,
        })
    for purchase in latest_purchases:
        latest_activity.append({
            'date': purchase.date,
            'type': 'Purchase',
            'reference': purchase.order_id,
            'amount': purchase.cost,
            'status': purchase.payment_status,
        })
    for dispatch in latest_dispatches:
        latest_activity.append({
            'date': dispatch.date,
            'type': 'Dispatch',
            'reference': dispatch.order_id,
            'amount': 0,
            'status': dispatch.status,
        })

    latest_activity = sorted(latest_activity, key=lambda x: x['date'], reverse=True)[:6]

    return render(request, 'core/dashboard.html', {
        'sales_total': sales_total,
        'purchase_total': purchase_total,
        'dispatch_pending': dispatch_pending,
        'procurement_qty': procurement_qty,
        'farmer_count': farmer_count,
        'latest_activity': latest_activity,
    })


def sales_page(request):
    sales = Sale.objects.order_by('-date')
    return render(request, 'core/sales.html', {'sales': sales})


def purchase_page(request):
    purchases = Purchase.objects.order_by('-date')
    return render(request, 'core/purchase.html', {'purchases': purchases})


def dispatch_page(request):
    dispatches = Dispatch.objects.order_by('-date')
    return render(request, 'core/dispatch.html', {'dispatches': dispatches})


def farmers_page(request):
    farmers = Farmer.objects.select_related('federation').all()
    return render(request, 'core/farmers.html', {'farmers': farmers})


def procurement_page(request):
    procurements = Procurement.objects.order_by('-date')
    return render(request, 'core/procurement.html', {'procurements': procurements})


def payments_page(request):
    payments = FarmerPayment.objects.order_by('-date')
    return render(request, 'core/payments.html', {'payments': payments})


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticated]


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAdminUser]


class DispatchViewSet(viewsets.ModelViewSet):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer
    


class ProcurementViewSet(viewsets.ModelViewSet):
    queryset = Procurement.objects.all()
    serializer_class = ProcurementSerializer
    
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAdminUser]


class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAdminUser]


class FarmerPaymentViewSet(viewsets.ModelViewSet):
    queryset = FarmerPayment.objects.all()
    serializer_class = FarmerPaymentSerializer
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAdminUser]


class FederationViewSet(viewsets.ModelViewSet):
    queryset = Federation.objects.all()
    serializer_class = FederationSerializer
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAdminUser]
