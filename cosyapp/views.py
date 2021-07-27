from django.db.models import query
from django.views.generic import ListView
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import PartSerializer, ProjectSerializer, TaskSerializer, UploadSerializer
from rest_framework import viewsets
from .models import Project, Part, Task

# Create your views here.
class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

# Do I need this Upload View at all?
class UploadView(viewsets.ModelViewSet):
    serializer_class = UploadSerializer
    queryset = Project.photo

# class UploadList(ListView):
#     model = Project
class PartView(viewsets.ModelViewSet):
    serializer_class = PartSerializer
    queryset = Part.objects.all()

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
