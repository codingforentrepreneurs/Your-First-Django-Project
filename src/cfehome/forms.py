from django import forms


class LandingPageForm(forms.Form):
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