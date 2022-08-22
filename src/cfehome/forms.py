from django import forms


class LandingPageForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    email2 = forms.EmailField(label='Confirm Email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            default_css_class = 'form-control' # bootstrap
            new_attrs = {
                "class": default_css_class,
                "id": f"{field}",
                "placeholder": f"Your {field}",
            }
            if field == "email2":
                new_attrs['placeholder'] = f"Confirm your email"
            self.fields[field].widget.attrs.update(new_attrs)


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