from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from contests.forms import ContestEntryForm
from contests.models import Contest, ContestEntry, ContestWinner


def enter(request):
    """
    Renders and processes contest entry page
    """
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

            return HttpResponseRedirect(reverse("contests_share"))
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
    winners = ContestWinner.objects.all()

    return render_to_response("contests/winners.html", {
        "winners": winners,
    }, context_instance=RequestContext(request))
