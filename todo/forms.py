from django import forms

class TextForm(forms.Form):
    text=forms.TextField(default="")