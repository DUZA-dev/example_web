from rest_framework import serializers

from event.models import Event, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    users = serializers.ModelSerializer(many=True, required=False, source='event.users')

    class Meta(object):
        model = Organization
        fields = ['title', 'description', 'full_address', 'users']


class EventSerializer(serializers.ModelSerializer):
    organizations = OrganizationSerializer(many=True, required=False)

    class Meta(object):
        model = Event
        fields = ['title', 'description', 'image', 'date', 'organizations']
