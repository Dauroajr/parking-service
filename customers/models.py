import re

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


def validate_cpf_format(value):
    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', value):
        raise ValidationError('CPF must be in XXX.XXX.XXX-XX format.')


class Customer(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="customers",
        verbose_name=_("User"),
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("Name"),
    )
    registration_number = models.CharField(
        max_length=18,
        blank=True,
        null=True,
        verbose_name=_("CPF"),
        # validators=[validate_cpf_format]
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name=_("Telephone")
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
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name
