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


class AssociatedMeetingCharFilter(filters.CharFilter):
    def global_q(self):
        """
        Uses the global filter to search a meeting field of meetings owned by the logged in user
        """
        if not self._global_search_value:
            return Q()
        kw = "meeting__{}__{}".format(self.field_name, self.lookup_expr)
        return Q(**{
            kw: self._global_search_value,
            "meeting__user_id": self.parent.request.user.id or -1,
        })


class ExpertGlobalFilterSet(DatatablesFilterSet):
    name = GlobalCharFilter(lookup_expr='icontains')
    objectives = AssociatedMeetingCharFilter(field_name='objective', lookup_expr='icontains')

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


class HomePageView(TemplateView):
    template_name = 'pages/home.html'