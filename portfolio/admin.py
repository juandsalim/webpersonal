from django.contrib import admin
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin): #clase para que se muestre en solo lectura los campos creted y updated
   readonly_fields = ('created', 'updated') 



admin.site.register(Project, ProjectAdmin)

