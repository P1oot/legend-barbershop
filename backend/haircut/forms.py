from django.forms import ModelForm
from .models import Services


class ServiceFaorm(ModelForm):
    class Meta:
        model = Services
        fields = ('name', 'price', 'description')
