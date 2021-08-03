from rest_framework import serializers
from .models import Project, Part, Task, ToBuyItem

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'description', 'completed', 'part')
        # depth = 2
class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'name', 'completed', 'project')
        # depth = 1

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'series', 'due_date', 'budget', 'completed', 'photo')

class ToBuyItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToBuyItem
        fields = ('id', 'description', 'price', 'link', 'completed', 'project')
