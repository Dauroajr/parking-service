from django.db import models
from django.utils.translation import gettext_lazy as _

from customers.models import Customer


COLOR_CHOICES = (
    ("Black", _("Black")),
    ("Blue", _("Blue")),
    ("Carbon", _("Carbon")),
    ("Grafite", _("Grafite")),
    ("Gray", _("Gray")),
    ("Green", _("Green")),
    ("Lime", _("Lime")),
    ("Maroon", _("Maroon")),
    ("Orange", _("Orange")),
    ("Pearl", _("Pearl")),
    ("Purple", _("Purple")),
    ("Red", _("Red")),
    ("Silver", _("Silver")),
    ("White", _("White")),
    ("Yellow", _("Yellow")),
)


class VehicleType(models.Model):

    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name=_("Vehicle Type"),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description")
    )

    class Meta:
        verbose_name = _("Vehicle Type")
        verbose_name_plural = _("Vehicle Types")

    def __str__(self):
        return self.name


class Brand(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name


class Vehicle(models.Model):

    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name=_("vehicles"),
        verbose_name=_("Vehicle Type")
    )
    license_plate = models.CharField(
        max_length=12,
        unique=True,
        verbose_name=_("License Plate"),
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name=_("Car Make"),
    )
    model = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_("Car Model")
    )
    color = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        choices=COLOR_CHOICES,
        verbose_name=_("Car Color")
    )
    owner = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name=_("vehicles"),
        verbose_name=_("Car Owner"),
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created on"),
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated on"),
    )

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")

    @property
    def full_model_name(self):
        return f"{self.brand} {self.model}"

    def __str__(self):
        return self.license_plate
