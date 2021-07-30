from django.contrib import admin
from .models import Project, Part, Task, ToBuyItem

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list = ('id', 'title', 'series', 'due_date', 'budget', 'completed', 'photo')

class PartAdmin(admin.ModelAdmin):
    list = ('id', 'name', 'project')

class TaskAdmin(admin.ModelAdmin):
    list = ('id', 'description', 'completed', 'part')

class ToBuyItemAdmin(admin.ModelAdmin):
    list = ('id', 'description', 'price', 'link', 'completed', 'project')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(ToBuyItem, ToBuyItemAdmin)
