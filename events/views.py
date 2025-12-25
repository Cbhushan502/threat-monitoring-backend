from rest_framework.generics import CreateAPIView
from .models import Event
from .serializers import EventSerializer


class EventCreateAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    