from django.forms import ModelForm
from .models import Services, Haircuts


class ServiceForm(ModelForm):
    class Meta:
        model = Services
        fields = ('name', 'price', 'description')


class HaircutsForm(ModelForm):
    class Meta:
        model = Haircuts
        fields = ('image',)
