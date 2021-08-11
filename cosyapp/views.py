from django.db.models import query
from django.http.response import HttpResponseRedirect
from django.utils.functional import new_method_proxy
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import Http404, HttpResponseRedirect
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import PartSerializer, ProjectSerializer, TaskSerializer, ToBuyItemSerializer, RegisterUserSerializer, MyTokenObtainPairSerializer
from rest_framework import viewsets, status, generics, permissions, status, response
from .models import Project, Part, Task, ToBuyItem

# Create your views here.

# @api_view(['GET'])
# def get_current_user(request):
#     serializer = RegisterUserSerializer(request.user)

#     return Response(serializer.data)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status.HTTP_201_CREATED)
        except Exception as e:
            return Response(status.HTTP_400_BAD_REQUEST)

# def home(request):
#     return render(request, 'home.html')

# @api_view(['GET'])
# def project_list(request):
#     currentUser = request.user
#     print(currentUser)
#     projects = Project.objects.filter(owner_id=currentUser.id)
#     serializer = ProjectSerializer(projects, many=True)
#     return Response(serializer.data)
class ProjectList(APIView):
    permission_classes = [AllowAny]
    '''
    List all projects, or create a new project
    '''
    parser_classes = (MultiPartParser, FormParser)
    # serializer_class = ProjectSerializer

    # returning AnonymousUser for the username and None for the id
    # do I need to make a post request to find which user id is currently authenticated before doing this get request?
    def get_queryset(self, request):
        currentUser = request.user #self.request.user?
        print(request)
        print(currentUser)
        print(currentUser.id)
        userProjects = Project.objects.filter(owner_id=currentUser.id).order_by('id')

        return userProjects
        # return Project.objects.filter(owner=self.kwargs.get('owner_id')).order_by('id')

    def get(self, request, format=None):
        projects = self.get_queryset(request)
        # projects = Project.objects.all().order_by('id')
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):
    permission_classes = [AllowAny]
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

class ProjectPartsList(generics.ListCreateAPIView): # should this be ListCreateAPIView? or ListAPIView?
    permission_classes = [AllowAny]
    serializer_class = PartSerializer

    def get_queryset(self):
        return Part.objects.filter(project=self.kwargs.get('pk')).order_by('id')

    def post(self, request, pk):
        print(request.data)
        part = Part(name=request.data["name"], project=Project.objects.get(id=pk))

        serializer = PartSerializer(part, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PartList(APIView):
    permission_classes = [AllowAny]
    '''
    List all projects, or create a new project
    '''
    def get(self, request, format=None):
        parts = Part.objects.all().order_by('id')
        serializer = PartSerializer(parts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProjectPartDetail(generics.ListAPIView):
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
class PartTasksList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(part=self.kwargs.get('pk')).order_by('id')

    # def post(self, request, format=None):
    #     serializer = TaskSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskList(APIView):
    permission_classes = [AllowAny]
    '''
    List all parts, or create a new part
    # '''
    # def get(self, request, format=None):
    #     tasks = Task.objects.all()
    #     serializer = TaskSerializer(tasks, many=True)
    #     return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    permission_classes = [AllowAny]
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

    def patch(self, request, pk, format=None):
        task = self.get_task(pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_task(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectToBuyList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ToBuyItemSerializer

    def get_queryset(self):
        return ToBuyItem.objects.filter(project=self.kwargs.get('pk')).order_by('id')

class ToBuyList(APIView):
    permission_classes = [AllowAny]
    '''
    List all parts, or create a new part
    '''
    # def get(self, request, format=None):
    #     items = ToBuyItem.objects.all()
    #     serializer = ToBuyItemSerializer(items, many=True)
    #     return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ToBuyItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToBuyListDetail(APIView):
    permission_classes = [AllowAny]

    def get_item(self, pk):
        try:
            return ToBuyItem.objects.get(pk=pk)
        except ToBuyItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_item(pk)
        serializer = ToBuyItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = self.get_item(pk)
        serializer = ToBuyItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        item = self.get_item(pk)
        serializer = ToBuyItemSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_item(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PartDetail(APIView):
    permission_classes = [AllowAny]
    """
    Retrieve, update, or delete a task instance.
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

    def patch(self, request, pk, format=None):
        part = self.get_part(pk)
        serializer = PartSerializer(part, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        part = self.get_part(pk)
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def post(self, request, format=None):
    #     serializer = ToBuyItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProjectView(viewsets.ModelViewSet):
#     serializer_class = ProjectSerializer
#     queryset = Project.objects.all()

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

# @api_view(['GET'])
# def current_user(request):
#     """
#     Determine the current user by their token, and return their data
#     """

#     serializer = UserSerializer(request.user)
#     return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CreateUserView(APIView):
#     permission_classes = (permissions.AllowAny, )

#     def post(self, request):
#         user = request.data.get('user')
#         if not user:
#             return Response({'response' : 'error', 'message': 'No data found'})
#         serializer = UserSerializerWithToken(data = user)

#         if serializer.is_valid():
#             saved_user = serializer.save()
#         else:
#             return Response({'response': 'error', 'message' : 'serializer.errors'})

#         return Response({'response' : 'success', 'message' : 'user created successfully'})


# from rest_framework import generics
# from blog.models import Post
# from .serializers import PostSerializer
# from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions


# class PostUserWritePermission(BasePermission):
#     message = 'Editing posts is restricted to the author only.'

#     def has_object_permission(self, request, view, obj):

#         if request.method in SAFE_METHODS:
#             return True

#         return obj.author == request.user


# class PostList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
