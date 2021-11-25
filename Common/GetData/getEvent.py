from apps.Event.models import Events


def get_event():
    events = Events.objects.filter(is_deleted=False)
    return events
