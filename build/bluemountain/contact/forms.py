from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    """
    A basic contact form
    """
    email = forms.EmailField(label=_("Email Address"))
    subject = forms.CharField(label=_("Subject"))
    message = forms.CharField(label=_("Message"), widget=forms.Textarea)
