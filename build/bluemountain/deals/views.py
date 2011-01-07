from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from deals.constants import DEALS_CACHE_KEY


def deals(request):
    """
    Renders deals page
    """
    return render_to_response("deals/list.html", {
        "deals": cache.get(DEALS_CACHE_KEY),
    }, context_instance=RequestContext(request))
