from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from contact.forms import ContactForm


def contact(request):
    """
    Renders contact us page
    """
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            send_mail(_("Contact Request"), render_to_string("contact/contact.txt", {
                "message": form.cleaned_data,
            }), settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])

            return HttpResponseRedirect(reverse("contact_thanks"))
    else:
        form = ContactForm()

    return render_to_response("contact/contact.html", {
        "form": form,
    }, context_instance=RequestContext(request))


def thanks(request):
    """
    Renders thank you page
    """
    return render_to_response("contact/thanks.html", {

    }, context_instance=RequestContext(request))
