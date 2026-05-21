from django.contrib import admin
from .models import Federation, Farmer, FarmerPayment, Procurement, Purchase, Sale, Dispatch

admin.site.register(Federation)
admin.site.register(Farmer)
admin.site.register(FarmerPayment)
admin.site.register(Procurement)
admin.site.register(Purchase)
admin.site.register(Sale)
admin.site.register(Dispatch)
