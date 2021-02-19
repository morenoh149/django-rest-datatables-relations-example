from rest_framework import serializers

from .models import Expert, Meeting
from accounts.serializers import UserSerializer


class ExpertSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Expert
        fields = (
            'id', 'name',
        )
        datatables_always_serialize = ('id',)


class MeetingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Meeting
        fields = (
            'id', 'objective',
        )
        datatables_always_serialize = ('id',)