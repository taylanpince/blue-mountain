from datetime import date
from BeautifulSoup import BeautifulStoneSoup, NavigableString
from urllib import urlopen

from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from django.utils.hashcompat import sha_constructor

from events.models import Event


class Command(BaseCommand):
    """
    Imports new events from an XML resource
    """
    args = "<path_or_url_to_xml>"
    help = "Imports new events from an XML resource"

    def handle(self, *args, **options):
        try:
            resource = urlopen(args[0])
        except IndexError:
            raise CommandError("You have to specify a file path or a URL.")

        soup = BeautifulStoneSoup(resource)

        for event in soup.findAll("event"):
            event_info = {
                "description": event.get("description", u""),
            }

            for attribute in event:
                if not isinstance(attribute, NavigableString):
                    event_info[attribute.name] = attribute.string or u""

            identifier = sha_constructor("%(description)s-%(date)s" % {
                "description": slugify(event_info.get("description").encode("utf-8")),
                "date": event_info.get("date", u"").encode("utf-8"),
            }).hexdigest().encode("utf-8")

            obj, created = Event.objects.get_or_create(identifier=identifier, defaults={
                "title": event_info.get("title", u"").encode("utf-8"),
                "content": event_info.get("body", u"").encode("utf-8"),
                "description": event_info.get("description").encode("utf-8"),
                "url": event_info.get("url", u"").encode("utf-8"),
                "order": int(event_info.get("displayorder", 0)),
                "date": date(
                    int(event_info.get("year", 0)),
                    int(event_info.get("month", 0)),
                    int(event_info.get("day", 0)),
                ),
            })
