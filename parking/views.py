from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from core.permissions import IsVehicleOrRecordOwner
from parking.models import ParkingSpot, ParkingRecords
from parking.serializers import ParkingSpotSerializer, ParkingRecordsSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):

    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [DjangoModelPermissions,]


class ParkingRecordsViewSet(viewsets.ModelViewSet):

    queryset = ParkingRecords.objects.all()
    serializer_class = ParkingRecordsSerializer
    permission_classes = [DjangoModelPermissions, IsVehicleOrRecordOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ParkingRecords.objects.all()
        return ParkingRecords.objects.filter(vehicle__owner__user=user)
