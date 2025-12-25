from alerts.models import Alert


def generate_alert(event):
    if event.severity in ['High', 'Critical']:
        Alert.objects.create(event=event)
