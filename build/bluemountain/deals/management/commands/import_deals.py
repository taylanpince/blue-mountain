from datetime import date
from BeautifulSoup import BeautifulStoneSoup
from urllib import urlopen

from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError

from deals.constants import *


class Command(BaseCommand):
    """
    Imports latest deals and updates cached data
    """
    def handle(self, *args, **kwargs):
        resource = urlopen(DEALS_URL)
        soup = BeautifulStoneSoup(resource)
        deals = []

        for deal in soup.findAll("deal"):
            deals.append({
                "category": deal.get("category"),
                "title": deal.find("title").text,
                "description": deal.find("description").text,
                "date": deal.find("date").text,
                "price": deal.find("price").text,
            })

        cache.set(DEALS_CACHE_KEY, deals, 7 * 24 * 60 * 60)
