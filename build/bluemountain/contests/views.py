from datetime import datetime, timedelta

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from contests.forms import ContestEntryForm
from contests.models import Contest, ContestEntry, ContestWinner
from content_blocks.models import Photo


CONTEST_COOKIE_KEY = "BLUEMOUNTAIN_CONTEST"


def enter(request):
    """
    Renders and processes contest entry page
    """
    if request.COOKIES.has_key(CONTEST_COOKIE_KEY):
        return HttpResponseRedirect(reverse("contests_share"))

    try:
        now = datetime.now()
        contest = Contest.objects.filter(
            start_date__lte=now,
            end_date__gte=now,
        )[0]
    except IndexError:
        contest = None

    if contest is None:
        return render_to_response("contests/closed.html", {
            
        }, context_instance=RequestContext(request))

    if request.method == "POST":
        form = ContestEntryForm(request.POST, contest=contest)

        if form.is_valid():
            contest_entry = form.save(commit=False)
            contest_entry.contest = contest
            contest_entry.save()

            response = HttpResponseRedirect(reverse("contests_share"))
            delta = contest.end_date - datetime.now()
            max_age = (delta.days * 24 * 60 * 60) + delta.seconds
            expiry = datetime.strftime(contest.end_date, "%a, %d-%b-%Y %H:%M:%S GMT")

            response.set_cookie(CONTEST_COOKIE_KEY, value="True", max_age=max_age, expires=expiry)

            return response
    else:
        form = ContestEntryForm()

    return render_to_response("contests/entry.html", {
        "form": form,
    }, context_instance=RequestContext(request))


def share(request):
    """
    Renders share/thank you page
    """
    return render_to_response("contests/share.html", {

    }, context_instance=RequestContext(request))


def rules(request):
    """
    Renders contest rules page
    """
    return render_to_response("contests/rules.html", {

    }, context_instance=RequestContext(request))


def winners(request):
    """
    Renders a list of winners, separated by contest
    """
    winners = ContestWinner.objects.order_by("-contest__start_date")

    return render_to_response("contests/winners.html", {
        "winners": winners,
    }, context_instance=RequestContext(request))


def photos(request):
    """
    Renders photos
    """
    photos = Photo.objects.all()

    return render_to_response("contests/photos.html", {
        "photos": photos,
    }, context_instance=RequestContext(request))
