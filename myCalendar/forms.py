from django import forms

class UserForm(forms.Form):
    month = forms.CharField(max_length=50, required=True)
    holidays = forms.CharField(max_length=100, required=False, help_text="(comma seperated)")
