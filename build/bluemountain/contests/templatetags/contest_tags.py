from datetime import datetime, timedelta

from django import template

from contests.models import Contest


register = template.Library()


@register.inclusion_tag("contests/countdown.html")
def contest_countdown():
    """
    Renders a countdown to the next available contest
    """
    try:
        contest = Contest.objects.filter(
            start_date__gt=datetime.now(),
        ).order_by("start_date")[0]
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
