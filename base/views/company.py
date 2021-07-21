from rest_framework import viewsets
from base.serializers.company import CompanySerializer
from base.models.company import Company


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
