from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from apps.company.serializers import WorkHoursSerializer
from apps.company.models import WorkHours
from apps.authentication.permissions import ConfirmedAccountPermission


class WorkHoursViewSet(viewsets.ModelViewSet):
    queryset = WorkHours.objects.all()
    serializer_class = WorkHoursSerializer
    permission_classes = [IsAuthenticated, ConfirmedAccountPermission]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
