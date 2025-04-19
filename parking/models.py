from django.db import models
from django.utils.translation import gettext_lazy as _

from vehicles.models import Vehicle


class ParkingSpot(models.Model):

    spot_number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name=_("Spot Number"),
    )
    is_occupied = models.BooleanField(default=False, verbose_name=_("Occupied"))
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created on"),
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated on"),
    )

    class Meta:
        verbose_name = _("Parking Spot")
        verbose_name_plural = _("Parking Spots")

    def __str__(self):
        return self.spot_number


class ParkingRecords(models.Model):

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name=_("parking_reords"),
        verbose_name=_("Vehicle"),
    )
    parking_spot = models.ForeignKey(
        ParkingSpot,
        on_delete=models.PROTECT,
        related_name=_("parking_reords"),
        verbose_name=_("Parking Spot"),
    )
    entry_time = models.DateTimeField(auto_now_add=True, verbose_name=_("Entry Time"))
    exit_time = models.DateTimeField(blank=True, null=True, verbose_name=_("Exit Time"))
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created on"),
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated on"),
    )

    class Meta:
        verbose_name = _("Record")
        verbose_name_plural = _("Records")

    def __str__(self):
        return f"{self.vehicle} - {self.parking_spot} - {self.entry_time}"
