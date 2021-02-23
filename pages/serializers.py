from rest_framework import serializers

from .models import Expert, Meeting
from accounts.serializers import UserSerializer


class ExpertSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    objectives = serializers.SerializerMethodField()

    class Meta:
        model = Expert
        fields = (
            'id', 'name', 'objectives'
        )
        datatables_always_serialize = ('id',)

    def get_objectives(self, obj):
        request = self.context["request"]
        meetings = Meeting.objects.filter(
            user_id=request.user.id, expert_id=obj.id
        ).distinct('objective')
        if len(meetings) > 0:
            objectives = meetings.values_list("objective", flat=True)
            objectives = ", ".join([x for x in objectives if x])
        else:
            objectives = []
        return objectives


class MeetingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Meeting
        fields = (
            'id', 'objective',
        )
        datatables_always_serialize = ('id',)