from django import forms

from .models import Customer


class CustomerAdminForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["registration_number"].widget.attrs.update({"class": "cpf-cnpj-mask"})
