import csv

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _


def export_csv(modeladmin, request, queryset):
    """
    Generic csv export admin action.
    """
    if not request.user.is_staff:
        raise PermissionDenied

    opts = modeladmin.model._meta
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]

    # Write a first row with header information
    writer.writerow(field_names)

    # Write data rows
    for obj in queryset:
        writer.writerow([unicode(getattr(obj, field)).encode("utf-8") for field in field_names])

    return response

export_csv.short_description = _("Export CSV")
