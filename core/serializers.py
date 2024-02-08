import phonenumbers

from rest_framework import serializers

from core.models import User
from event.serializers import OrganizationSerializer


class UserSerializer(serializers.ModelSerializer):
    """ Сериализация переопределенной модели User """
    organizations = OrganizationSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ('email', 'telephone', 'password', 'organizations', )
        extra_kwargs = {
            'password': {'write_only': True, },
        }

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)

        return user

    def validate_telephone(self, value: str) -> str:
        """
        Валидация мобильного/домашнего/виртуального номера
        с помошью гугловской библиотеки phonenumbers
        """
        if value is None:
            return value
        elif value[0] != '+':
            value = f'+{value}'

        telephone = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(telephone):
            raise serializers.ValidationError("Введите корректный номер телефона")
        return value
