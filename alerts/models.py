from django.db import models
from events.models import Event


class Alert(models.Model):
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Acknowledged', 'Acknowledged'),
        ('Resolved', 'Resolved'),
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='alerts'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for Event {self.event.id} - {self.status}"
