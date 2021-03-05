from django.views.generic import TemplateView

from django_filters import filters
from rest_framework import viewsets
from rest_framework_datatables.django_filters.backends import DatatablesFilterBackend
from rest_framework_datatables.django_filters.filterset import DatatablesFilterSet
from rest_framework_datatables.django_filters.filters import GlobalFilter

from pages.models import Expert, Meeting
from pages.serializers import ExpertSerializer, MeetingSerializer


class GlobalCharFilter(GlobalFilter, filters.CharFilter):
    pass

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class ExpertGlobalFilterSet(DatatablesFilterSet):
    name = GlobalCharFilter(lookup_expr='icontains')
    objectives = GlobalCharFilter(field_name='meeting__objective', lookup_expr='icontains')

    class Meta:
        model = Expert
        fields = '__all__'

class ExpertViewSet(viewsets.ModelViewSet):
    queryset = Expert.objects.all().order_by("id")
    serializer_class = ExpertSerializer
    filter_backends = (DatatablesFilterBackend,)
    filterset_class = ExpertGlobalFilterSet


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all().order_by("id")
    serializer_class = MeetingSerializer
    permission_classes = []
    filterset_fields = []