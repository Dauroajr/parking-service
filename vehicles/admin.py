from django.contrib import admin

from vehicles.models import Brand, Vehicle, VehicleType


# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     """Admin View for Brand"""

#     list_display = ("name",)
#     list_filter = ("name",)
#     search_fields = ("name",)


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):

    list_display = ["name", "description"]
    search_fields = [
        "name__icontains",
    ]


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    list_display = [
        "full_model_name",
        "vehicle_type",
        "license_plate",
        "color",
        "owner",
    ]
    search_fields = [
        "license_plate__icontains",
        "model__icontains",
    ]
    list_filter = [
        "vehicle_type",
    ]
