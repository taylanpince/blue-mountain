from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    """
    An event with date, description, and URL
    """
    identifier = models.CharField(_("Identifier"), max_length=255, unique=True, db_index=True)
    title = models.CharField(_("Title"), blank=True, max_length=255)
    content = models.TextField(_("Content"), blank=True)
    description = models.CharField(_("Description"), blank=True, max_length=255)
    date = models.DateField(_("Date"), blank=True, null=True)
    url = models.URLField(_("URL"), blank=True, null=True, verify_exists=False)
    order = models.PositiveSmallIntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ["order"]

    def __unicode__(self):
        return self.title
