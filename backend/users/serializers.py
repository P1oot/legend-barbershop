from rest_framework import serializers, validators
from phonenumber_field.serializerfields import PhoneNumberField

from .models import User


class UserSerialixer(serializers.ModelSerializer):
    phone = PhoneNumberField(
        validators = [validators.UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        validators = [validators.UniqueValidator(queryset=User.objects.all())]
    )
    class Meta:
        model = User
        fields = (
            'phone',
            'email',
            'first_name',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }