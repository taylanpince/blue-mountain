from django.db import models
from django.utils.translation import ugettext_lazy as _


class ContentBlock(models.Model):
    """
    A piece of text-based content that can be placed anywhere on the site
    """
    title = models.CharField(_("Name"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    content = models.TextField(_("Content"), blank=True)

    class Meta:
        verbose_name = _("Content Block")
        verbose_name_plural = _("Content Blocks")

    def __unicode__(self):
        return self.title


class Photo(models.Model):
    """
    A photo with a caption
    """
    image = models.ImageField(_("Image"), upload_to="files/photos")
    caption = models.CharField(_("Caption"), blank=True, max_length=255)

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")

    def __unicode__(self):
        return self.caption
