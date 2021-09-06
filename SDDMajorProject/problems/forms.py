from django import forms

class Code (forms.Form):
    code = forms.CharField(widget=forms.Textarea)

    def clean_code (self):
        data = self.cleaned_data["code"]

        return data