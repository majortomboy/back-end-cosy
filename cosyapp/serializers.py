from rest_framework import serializers
from .models import Project, Part, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'series', 'due_date', 'budget', 'completed', 'photo')

class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('photo')

class PartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Part
        fields = ('id', 'name', 'project')

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'description', 'completed', 'part')
