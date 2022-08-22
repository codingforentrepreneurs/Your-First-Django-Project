from django import forms

from . import mixins
from .models import LandingPageEntry

class EntryNotesModelForm(mixins.BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = LandingPageEntry
        fields = ["name", "email", "notes"]


class LandingPageEntryModelForm(mixins.BootstrapFormMixin, forms.ModelForm):
    name = forms.CharField(required=False)
    email2 = forms.EmailField(label='Confirm Email')

    class Meta:
        model = LandingPageEntry
        fields = ["name", "email"]

    def clean(self):
        data = self.cleaned_data
        email = data.get("email")
        email2 = data.get("email2")
        if email2 != email:
            # self.add_error('email', 'Your email must match!')
            raise forms.ValidationError("Your email must match")
        return data


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email.endswith('gmail.com'):
            self.add_error('email', 'You cannot use gmail seriously!')
            # raise forms.ValidationError("Your cannot use gmail")
        return email



class LandingPageForm(mixins.BootstrapFormMixin, forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    email2 = forms.EmailField(label='Confirm Email')

    def clean(self):
        data = self.cleaned_data
        email = data.get("email")
        email2 = data.get("email2")
        if email2 != email:
            # self.add_error('email', 'Your email must match!')
            raise forms.ValidationError("Your email must match")
        return data


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email.endswith('gmail.com'):
            self.add_error('email', 'You cannot use gmail seriously!')
            # raise forms.ValidationError("Your cannot use gmail")
        return email