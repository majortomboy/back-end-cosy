from django.db.models import query
from django.shortcuts import render
from .serializers import PartSerializer, ProjectSerializer, TaskSerializer
from rest_framework import viewsets
from .models import Project, Part, Task

# Create your views here.
class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class PartView(viewsets.ModelViewSet):
    serializer_class = PartSerializer
    queryset = Part.objects.all()

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
