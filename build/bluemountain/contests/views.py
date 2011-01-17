from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from django_mobile import get_flavour

from contests.choices import SOURCE_DESKTOP, SOURCE_MOBILE
from contests.forms import ContestEntryForm, EmailForm, ValidatingFormSet
from contests.models import Contest, ContestEntry, ContestWinner
from content_blocks.models import Photo


CONTEST_COOKIE_KEY = "BLUEMOUNTAIN_CONTEST"
CONTEST_FIRST_NAME_KEY = "BLUEMOUNTAIN_CONTEST_FIRST_NAME"


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

            if get_flavour(request=request) == u"mobile":
                contest_entry.source = SOURCE_MOBILE
            else:
                contest_entry.source = SOURCE_DESKTOP

            contest_entry.save()

            response = HttpResponseRedirect(reverse("contests_share"))
            delta = contest.end_date - datetime.now()
            max_age = (delta.days * 24 * 60 * 60) + delta.seconds
            expiry = datetime.strftime(contest.end_date, "%a, %d-%b-%Y %H:%M:%S GMT")

            response.set_cookie(CONTEST_COOKIE_KEY, value="True", max_age=max_age, expires=expiry)
            response.set_cookie(CONTEST_FIRST_NAME_KEY, value=form.cleaned_data.get("first_name"), max_age=max_age, expires=expiry)

            return response
    else:
        form = ContestEntryForm()

    return render_to_response("contests/enter.html", {
        "form": form,
    }, context_instance=RequestContext(request))


def share(request):
    """
    Renders share/thank you page
    """
    ShareFormSet = formset_factory(EmailForm, formset=ValidatingFormSet, extra=3)

    if request.method == "POST":
        formset = ShareFormSet(request.POST)

        if formset.is_valid():
            emails = []

            for form_data in formset.cleaned_data:
                email = form_data.get("email", None)

                if email:
                    emails.append(email)

            if request.COOKIES.has_key(CONTEST_FIRST_NAME_KEY):
                name = request.COOKIES.get(CONTEST_FIRST_NAME_KEY)
            else:
                name = u"Someone"

            send_mail("Chopper to the top of Blue Mountain with %s" % name, render_to_string("contests/share.txt", {
                "site": Site.objects.get_current(),
                "name": name,
            }), settings.DEFAULT_FROM_EMAIL, emails)

            return HttpResponseRedirect(reverse("contests_thanks"))
    else:
        formset = ShareFormSet()

    return render_to_response("contests/share.html", {
        "formset": formset,
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
        "contests": Contest.objects.all(),
    }, context_instance=RequestContext(request))


def photos(request):
    """
    Redirects to prizes
    """
    return HttpResponseRedirect(reverse("contests_prizes"))


def thanks(request):
    """
    Renders thank you page
    """
    return render_to_response("contests/thanks.html", {

    }, context_instance=RequestContext(request))


def prizes(request):
    """
    Renders prizes page
    """
    photos = Photo.objects.all()

    return render_to_response("contests/prizes.html", {
        "photos": photos,
    }, context_instance=RequestContext(request))
