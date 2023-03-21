from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .serializers import CompanySerializer
from .models import Company


class CompanyViewset(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination
