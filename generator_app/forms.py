from django import forms

class PassForm(forms.Form):
    to = forms.CharField(label="Your Choice", max_length=32)
    length = forms.IntegerField(label="Password Length")