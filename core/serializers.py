from rest_framework import serializers
from .models import Federation, Farmer, FarmerPayment, Procurement, Purchase, Sale, Dispatch


class FederationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Federation
        fields = '__all__'


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'


class FarmerPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerPayment
        fields = '__all__'


class ProcurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procurement
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class DispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatch
        fields = '__all__'
