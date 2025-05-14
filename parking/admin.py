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
    search_fields = ("spot_number__icontains",)
    ordering = [
        "spot_number",
    ]


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
        "vehicle__license_plate__icontains",
        "parking_spot__spot_number__icontains",
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if (
            db_field.name == "parking_spot" and not request.resolver_match.url_name.endswith("change")
        ):
            kwargs["queryset"] = ParkingSpot.objects.filter(is_occupied=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # In order to make the 'parking_spot' field a read_only, uncomment the block below
    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return self.readonly_fields + ("parking_spot",)
    #     return super().get_readonly_fields(request, obj)
