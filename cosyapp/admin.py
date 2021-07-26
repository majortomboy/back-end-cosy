from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list = ('id', 'title', 'series', 'due_date', 'budget', 'completed')

admin.site.register(Project, ProjectAdmin)
