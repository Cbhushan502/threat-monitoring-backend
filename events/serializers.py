from rest_framework import serializers
from .models import Event
from .services import generate_alert


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['created_at']

    def create(self, validated_data):
        event = super().create(validated_data)
        generate_alert(event)
        return event
    