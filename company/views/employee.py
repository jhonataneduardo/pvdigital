from rest_framework import permissions, generics
from rest_framework.response import Response

from company.serializers.employee import EmployeeSerializer
from company.models.employee import Employee


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ['company']

    # def get_queryset(self):
    #     return Employee.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)


class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
