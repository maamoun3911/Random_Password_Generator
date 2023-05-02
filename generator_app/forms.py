from django import forms

class PassForm(forms.Form):
    social_choice = forms.CharField(label="Your Choice", max_length=32)
    pass_length = forms.IntegerField(label="Password Length")