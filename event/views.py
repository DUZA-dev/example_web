from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from django_filters import DateTimeFilter, filterset
from django_filters.rest_framework import DjangoFilterBackend

from event.models import Event, Organization
from event.serializers import EventSerializer, OrganizationSerializer
from event.tasks import event_save


class EventFilter(filterset.FilterSet):
    date = DateTimeFilter(field_name='date', lookup_expr='date')
    date__gte = DateTimeFilter(field_name="date", lookup_expr='date__gte')
    date__lte = DateTimeFilter(field_name="date", lookup_expr='date__lte')

    class Meta:
        model = Event
        fields = []

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = EventSerializer

    filterset_class = EventFilter
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = ['title', ]
    ordering_fields = ['date', ]
    page_size_query_param = 'limit'

    def create(self, request, *args, **kwargs):
        event_save.delay(request.data, *args, **kwargs)
        return Response({'message': 'Created'}, status.HTTP_102_PROCESSING)


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = OrganizationSerializer
