from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from conditions.constants import TRAIL_REPORT_CACHE_KEY, WEATHER_REPORT_CACHE_KEY


def live(request):
    """
    Renders live resort conditions page
    """
    return render_to_response("conditions/live.html", {
        "weather": cache.get(WEATHER_REPORT_CACHE_KEY),
        "trails": cache.get(TRAIL_REPORT_CACHE_KEY),
    }, context_instance=RequestContext(request))


def trail_map(request):
    """
    Renders trail map page
    """
    return render_to_response("conditions/trail_map.html", {
        
    }, context_instance=RequestContext(request))
