from django.views.generic import TemplateView

from rest_framework import viewsets

from meetings.models import Expert, Meeting
from meetings.serializers import ExpertSerializer, MeetingSerializer


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class ExpertViewSet(viewsets.ModelViewSet):
    queryset = Expert.objects.all().order_by("id")
    serializer_class = ExpertSerializer
    permission_classes = []


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all().order_by("id")
    serializer_class = MeetingSerializer
    permission_classes = []
    filterset_fields = []