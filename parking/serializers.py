from rest_framework import serializers

from parking.models import ParkingSpot, ParkingRecords


class ParkingSpotSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkingSpot
        fields = "__all__"


class ParkingRecordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkingRecords
        fields = "__all__"
