from django import forms

class PassForm(forms.Form):
    length = forms.IntegerField(label="Password Length")