from django import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from .views import (
    SaleViewSet,
    PurchaseViewSet,
    DispatchViewSet,
    ProcurementViewSet,
    FarmerViewSet,
    FarmerPaymentViewSet,
    FederationViewSet,
)

router = DefaultRouter()
router.register('sales', SaleViewSet)
router.register('purchases', PurchaseViewSet)
router.register('dispatches', DispatchViewSet)
router.register('procurements', ProcurementViewSet)
router.register('farmers', FarmerViewSet)
router.register('payments', FarmerPaymentViewSet)
router.register('federations', FederationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth-token/', obtain_auth_token, name='api_token_auth'),
    # path('profile/', views.user_profile, name='user_profile'),
    # path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
