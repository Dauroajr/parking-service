from django.contrib import admin

from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ["name", "registration_number", "phone_number", "created_on"]
    search_fields = ["name__icontains", "registration_number__icontains", "phone_number__icontains"]
