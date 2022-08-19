from django import forms


class LandingPageForm(forms.Form):
    # name = ??
    email = forms.EmailField()