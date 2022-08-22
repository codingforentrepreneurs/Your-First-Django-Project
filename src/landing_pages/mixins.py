

class BootstrapFormMixin(object):
    fields = []
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

