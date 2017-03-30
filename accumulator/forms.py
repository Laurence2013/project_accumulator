from django import forms

class AccumulatorForm(forms.Form):
    game = forms.BooleanField(required = False)
