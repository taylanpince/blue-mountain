import re

from datetime import datetime, timedelta

from django import template
from django.conf import settings

from contests.models import Contest, ContestWinner


register = template.Library()


@register.inclusion_tag("contests/winner.html")
def last_weeks_winner():
    """
    Renders last week's winner's photo
    """
    contests = Contest.objects.filter(
        flight_date__isnull=False,
        flight_date__lte=datetime.now(),
    ).order_by("-flight_date")

    winner = None

    if contests:
        for contest in contests:
            try:
                winner = contest.winners.all()[0]
            except IndexError:
                pass

            if winner is not None:
                break

    return {
        "winner": winner,
        "MEDIA_URL": settings.MEDIA_URL,
    }


@register.inclusion_tag("contests/countdown.html")
def contest_countdown():
    """
    Renders a countdown to the next available contest
    """
    try:
        contest = Contest.objects.filter(
            flight_date__gt=datetime.now(),
        ).order_by("flight_date")[0]
    except IndexError:
        contest = None

    return {
        "contest": contest,
    }


@register.filter
def countdown(target_date):
    """
    Returns a detailed countdown string to the given date
    """
    delta = target_date - datetime.now()
    hours, remainder = divmod(delta.seconds, 60 * 60)
    minutes, remainder = divmod(remainder, 60)

    return u"%(days)d days, %(hours)d hours, %(minutes)d minutes" % {
        "days": delta.days,
        "hours": hours,
        "minutes": minutes,
    }


class NextContestNode(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        try:
            contest = Contest.objects.filter(
                flight_date__gt=datetime.now(),
            ).order_by("flight_date")[0]
        except IndexError:
            contest = None

        context[self.var_name] = contest

        return ""


@register.tag
def next_contest(parser, token):
    """
    Gets next contest and injects it into the template context
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]

    m = re.search(r'as (\w+)', arg)

    if not m:
        raise template.TemplateSyntaxError, "%r had invalid arguments" % tag_name

    var_name, = m.groups()

    return NextContestNode(var_name)
