from rest_framework import serializers
from .models import Project, Part, Task
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'description', 'completed', 'part')
        # depth = 2
class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'name', 'project')
        # depth = 1

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'series', 'due_date', 'budget', 'completed', 'photo')
