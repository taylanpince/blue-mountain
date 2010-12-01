from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contest(models.Model):
    """
    A contest period with start and end dates
    """
    title = models.CharField(_("Title"), max_length=255)
    start_date = models.DateTimeField(_("Start Date"))
    end_date = models.DateTimeField(_("End Date"))

    class Meta:
        verbose_name = _("Contest")
        verbose_name_plural = _("Contests")

    def __unicode__(self):
        return self.title


class ContestEntry(models.Model):
    """
    An entry in a `Contest`, unique by email
    """
    contest = models.ForeignKey(Contest, verbose_name=_("Contest"), related_name="entries")
    email = models.EmailField(_("Email Address"), max_length=255)
    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    entry_date = models.DateTimeField(_("Entry Date"), auto_now_add=True)
    newsletter = models.BooleanField(_("Newsletter Subscription"), default=False)

    @property
    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = _("Contest Entry")
        verbose_name_plural = _("Contest Entries")
        unique_together = ("contest", "email")

    def __unicode__(self):
        return u"%s %s for %s" % (self.first_name, self.last_name, self.contest.title)


class ContestWinner(models.Model):
    """
    A winner in a contest
    """
    name = models.CharField(_("Name"), max_length=255)
    photo = models.ImageField(_("Photo"), upload_to="files/winners")
    contest = models.ForeignKey(Contest, verbose_name=_("Contest"), related_name="winners")

    class Meta:
        verbose_name = _("Contest Winner")
        verbose_name_plural = _("Contest Winners")

    def __unicode__(self):
        return self.name
