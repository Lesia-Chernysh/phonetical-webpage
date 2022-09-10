from django.contrib import admin

# Register your models here.
from .models import InformationAboutVowels
from .models import InformationAboutConsonants

admin.site.register(InformationAboutVowels)
admin.site.register(InformationAboutConsonants)
