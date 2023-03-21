from rest_framework import routers
from .views import CompanyViewset

companies_router = routers.DefaultRouter()
companies_router.register("companies", viewset=CompanyViewset, basename="companies")
