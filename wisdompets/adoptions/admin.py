from django.contrib import admin

<<<<<<< Updated upstream
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']
=======
# Register your models here.
>>>>>>> Stashed changes
