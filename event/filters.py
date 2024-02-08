from django_filters import DateTimeFilter, filterset

from event.models import Event


class EventFilter(filterset.FilterSet):
    """ Фильтр событий по дате """
    date = DateTimeFilter(field_name='date', lookup_expr='date')
    date__gte = DateTimeFilter(field_name="date", lookup_expr='date__gte')
    date__lte = DateTimeFilter(field_name="date", lookup_expr='date__lte')

    class Meta:
        model = Event
        fields = []
