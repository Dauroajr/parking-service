from django.contrib import admin

from parking.models import ParkingSpot, ParkingRecords


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    """Admin View for ParkingSpot"""

    list_display = (
        "spot_number",
        "is_occupied",
    )
    list_filter = ("is_occupied",)
    search_fields = ("spot_number",)


@admin.register(ParkingRecords)
class ParkingRecordsAdmin(admin.ModelAdmin):
    """Admin View for ParkingRecords"""

    list_display = (
        "vehicle",
        "parking_spot",
        "entry_time",
        "exit_time",
    )
    search_fields = (
        "vehicle__license_plate",
        "parking_spot__spot_number",
    )
