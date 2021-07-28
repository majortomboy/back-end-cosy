from django.db.models import query
from django.views.generic import ListView
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.urlpatterns import format_suffix_patterns
from .serializers import PartSerializer, ProjectSerializer, TaskSerializer
from rest_framework import viewsets, status, generics
from .models import Project, Part, Task

# Create your views here.

class ProjectList(APIView):
    '''
    List all projects, or create a new project
    '''
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class ProjectDetail(APIView):
    """
    Retrieve, update or delete a project instance
    """
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectPartsList(generics.ListAPIView):
    serializer_class = PartSerializer

    def get_queryset(self):
        return Part.objects.filter(project=self.kwargs.get('pk'))

# class PartList(APIView):
#     '''
#     List all projects, or create a new part
#     '''
#     def get(self, request, format=None):
#         parts = Part.objects.all()
#         serializer = PartSerializer(parts, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = PartSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class ProjectPartDetail(generics.ListAPIView):
    """
    Retrieve, update, or delete a part instance.
    """
    def get_part(self, pk):
        try:
            return Part.objects.get(pk=pk)
        except Part.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        part = self.get_part(pk)
        serializer = PartSerializer(part)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        part = self.get_part(pk)
        serializer = PartSerializer(part, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        part = self.get_part(pk)
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class PartDetail(APIView):
#     """
#     Retrieve, update, or delete a part instance.
#     """
#     def get_part(self, pk):
#         try:
#             return Part.objects.get(pk=pk)
#         except Part.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         part = self.get_part(pk)
#         serializer = PartSerializer(part)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         part = self.get_part(pk)
#         serializer = PartSerializer(part, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         part = self.get_part(pk)
#         part.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class PartTasksList(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(part=self.kwargs.get('pk'))
class TaskList(APIView):
    '''
    List all projects, or create a new part
    '''
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class TaskDetail(APIView):
    """
    Retrieve, update, or delete a task instance.
    """
    def get_task(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_task(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_task(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_task(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class ProjectView(viewsets.ModelViewSet):
#     serializer_class = ProjectSerializer
#     queryset = Project.objects.all()

# context = {'images' : img_list}
#     return render(request, "photo/index.html", context)


# class PartView(viewsets.ModelViewSet):
#     # serializer_class = PartSerializer
#     queryset = Part.objects.all()

#     def list(self, request, domain_pk=None):
#         queryset = self.queryset.filter(domain=domain_pk)
#         serializer = PartSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None, domain_pk=None):
#         queryset = self.queryset.get(pk=pk, domain=domain_pk)
#         serializer = PartSerializer(queryset)
#         return Response(serializer.data)

# class PartView(viewsets.ModelViewSet):
#     serializer_class = PartSerializer
#     queryset = Part.objects.all()

# class TaskView(viewsets.ModelViewSet):
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()

# Do I need this Upload View at all?
# class UploadView(viewsets.ModelViewSet):
#     serializer_class = UploadSerializer
#     queryset = Project.photo

# class UploadList(ListView):
#     model = Project
