from django import forms

class Form(forms.Form):
	text = forms.CharField(max_length=100)
