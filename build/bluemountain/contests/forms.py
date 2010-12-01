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

    email_confirm = forms.EmailField(_("Confirm Email"))

    class Meta:
        model = ContestEntry
        exclude = ("contest", "entry_date")

    def clean(self):
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
