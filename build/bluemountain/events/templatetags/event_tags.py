from datetime import date

from django import template

from events.models import Event


register = template.Library()


@register.inclusion_tag("events/upcoming.html")
def upcoming_events():
    """
    Renders a list of upcoming events
    """
    events = Event.objects.filter(
        date__gte=date.today(),
    ).order_by("date")[:10]

    return {
        "events": events,
    }
