from django import forms
from django.utils.translation import ugettext_lazy as _

from contests.models import ContestEntry


class ContestEntryForm(forms.ModelForm):
    """
    An entry form for a contest
    """
    def __init__(self, *args, **kwargs):
        self.contest = kwargs.pop("contest", None)

        super(ContestEntryForm, self).__init__(*args, **kwargs)

        self.fields.get("newsletter").label = _("Yes, please send me Blue Mountain deals and updates")
        self.fields.get("birth_date").label = _("Birth Date (YYYY-MM-DD)")
        self.fields.get("phone_number").label = _("Phone Number (123-123-1234)")

    email_confirm = forms.EmailField(label=_("Confirm Email Address"))
    agreement = forms.BooleanField(label=_("I Have Read The Rules*"))

    class Meta:
        model = ContestEntry
        exclude = ("contest", "entry_date")

    def clean(self):
        self.cleaned_data = super(ContestEntryForm, self).clean()

        if self.cleaned_data.get("email", None):
            try:
                duplicate_entry = ContestEntry.objects.get(
                    email__iexact=self.cleaned_data.get("email"),
                    contest=self.contest,
                )
            except ContestEntry.DoesNotExist:
                duplicate_entry = None

            if duplicate_entry is not None:
                raise forms.ValidationError(_("You cannot participate in this week's contest more than once."))

            if self.cleaned_data.get("email") != self.cleaned_data.get("email_confirm"):
                raise forms.ValidationError(_("Please make sure both emails match."))

        return self.cleaned_data


class EmailForm(forms.Form):
    """
    A form with a single email field
    """
    email = forms.EmailField(_("Email"))


class ValidatingFormSet(forms.formsets.BaseFormSet):
    """
    A FormSet that makes sure there is at least one object in it
    """
    def clean(self):
        cleaned_data = super(ValidatingFormSet, self).clean()
        has_object = False

        for form in self.forms:
            if hasattr(form, 'cleaned_data'):
                if form.cleaned_data and not form.cleaned_data.get("DELETE", False):
                    has_object = True

        if not has_object:
            raise forms.ValidationError(_(u"You have to enter at least one email."))

        return cleaned_data
