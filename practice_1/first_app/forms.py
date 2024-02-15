from django import forms
from django.forms.widgets import NumberInput


class ExampleForm(forms.Form):
	name = forms.CharField()
	# comment = forms.CharField(widget=forms.Textarea)
	comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
	email = forms.EmailField()
	birth_date= forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
	BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
	birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
	value = forms.DecimalField()
	message = forms.CharField(max_length = 10,)
	email_address = forms.EmailField(label="Please enter your email address",)
	first_name = forms.CharField(initial='Your name')
	agree = forms.BooleanField(initial=True)
	FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),]
	favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
	