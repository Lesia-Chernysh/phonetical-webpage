from django.contrib import admin

# Register your models here.
from .models import InformationAboutVowels
from .models import InformationAboutConsonants
from .models import Exercises

admin.site.register(InformationAboutVowels)
admin.site.register(InformationAboutConsonants)
admin.site.register(Exercises)
