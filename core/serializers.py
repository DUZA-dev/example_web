import phonenumbers

from rest_framework import serializers

from core.models import User
from event.serializers import OrganizationSerializer


class UserSerializer(serializers.ModelSerializer):
    organizations = OrganizationSerializer(many=True, required=False)

    class Meta(object):
        model = User
        fields = ['email', 'telephone', 'password', 'organizations']
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user

    def validate_telephone(self, value):
        if value is None:
            return value
        elif value[0] != '+':
            value = f'+{value}'

        telephone = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(telephone):
            raise serializers.ValidationError("Введите корректный номер телефона")
        return value
