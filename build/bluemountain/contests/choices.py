from django.utils.translation import ugettext_lazy as _


SOURCE_UNKNOWN = 0
SOURCE_DESKTOP = 1
SOURCE_MOBILE = 2

SOURCE_CHOICES = (
    (SOURCE_UNKNOWN, _("Unknown")),
    (SOURCE_DESKTOP, _("Desktop")),
    (SOURCE_MOBILE, _("Mobile")),
)
