from django import forms
from django.core import validators
import datetime

yearss = ['2020','2021','2022','2023']
COLOURS =[
    ('Blue','blue'),
    ('Red','red'),
    ('Green','green'),
    ('Black','black'),
]
FOODS = [
    ('Pizza','pizza'),
    ('Burger','burger'),
    ('Noodles','noodles'),
    ('Rice','rice'),
]
class StudentApply(forms.Form):
    name = forms.CharField(label='Student Name',  widget=forms.Textarea(attrs={'rows':2}))
    email = forms.EmailField(help_text='Enter your email address')
    HSC_Completed = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    passing_year = forms.DateField(widget=forms.SelectDateWidget(years=yearss))
    HSC_registration_number = forms.DecimalField()
    apply_date = forms.DateField(initial=datetime.date.today())
    favourite_color = forms.ChoiceField(widget=forms.RadioSelect,  choices=COLOURS)
    favourite_food = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FOODS)
    passport_image = forms.ImageField()
    
    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data) < 10:
            raise forms.ValidationError('Name must be at least 10 characters')
        return data
    
    
    