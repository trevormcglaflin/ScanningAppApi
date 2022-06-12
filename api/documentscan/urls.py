from django.urls import path
from . import views
from rest_framework_nested import routers

# URLConf
router = routers.DefaultRouter()
router.register('companies', views.CompanyViewSet, basename="companies")

companies_router = routers.NestedDefaultRouter(
    router, 'companies', lookup='company')
companies_router.register('documents', views.DocumentViewSet,
                         basename='company-documents')
companies_router.register('incomestatements', views.IncomeStatementViewSet,
                         basename='company-incomestatements')


urlpatterns = router.urls + companies_router.urls