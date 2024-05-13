from django import forms
from .models import InformationAboutVowels
from .models import InformationAboutConsonants
from .models import Exercises


class AudioForm(forms.ModelForm):
    class Meta:
        model = InformationAboutVowels
        fields=['documents']


class AudioForm1(forms.ModelForm):
    class Meta:
        model = InformationAboutConsonants
        fields=['documents']


class AudioForm2(forms.ModelForm):
    class Meta:
        model = Exercises
        fields=['documents']