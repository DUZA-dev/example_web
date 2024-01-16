from django.urls import path

from event.views import EventViewSet, OrganizationViewSet


urlpatterns = [
    path('events/', EventViewSet.as_view({'get': 'list'}), name='event-list'),
    path('events/<pk>', EventViewSet.as_view({'get': 'retrieve'}), name='event-detail'),
    path('events/create', EventViewSet.as_view({'post': 'create'}), name='event-create'),

    path('organizations/', OrganizationViewSet.as_view({'get': 'list'}), name='organization-list'),
    path('organizations/<pk>', OrganizationViewSet.as_view({'get': 'retrieve'}), name='organization-detail'),
    path('organizations/create', OrganizationViewSet.as_view({'post': 'create'}), name='organization-create')
]
