from datetime import date
from BeautifulSoup import BeautifulStoneSoup, Tag
from urllib import urlopen

from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError

from conditions.constants import *


class Command(BaseCommand):
    """
    Imports latest conditions and updates cached data
    """
    def handle(self, *args, **kwargs):
        resource = urlopen(TRAIL_REPORT_URL)
        soup = BeautifulStoneSoup(resource)
        lift = soup.find("lifts")
        
        cache.set(TRAIL_REPORT_CACHE_KEY, {
            "total": lift.get("total"),
            "open": lift.get("totalopen"),
        }, 7 * 24 * 60 * 60)

        resource = urlopen(WEATHER_REPORT_URL)
        soup = BeautifulStoneSoup(resource)
        report = soup.findAll("report")[1]
        forecast = []

        weather_data = {
            "temperature": report.get("temp"),
            "surface": report.get("surfaceconditions"),
        }

        for i in range(1, 5):
            day = soup.find("day%d" % i)

            if day:
                forecast.append({
                    "day": day.get("day"),
                    "status": WEATHER_TYPES[int(day.get("icon"))],
                })

        weather_data["forecast"] = forecast

        cache.set(WEATHER_REPORT_CACHE_KEY, weather_data, 7 * 24 * 60 * 60)
