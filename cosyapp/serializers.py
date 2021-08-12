from rest_framework import serializers
from rest_framework_jwt.serializers import User
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Project, Part, Task, ToBuyItem

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    #     return token
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        data['id'] = self.user.id
        # data['groups'] = self.user.groups.values_list('name', flat=True)
        return data

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
        fields = ('id', 'title', 'series', 'due_date', 'budget', 'completed', 'photo', 'owner')

class ToBuyItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToBuyItem
        fields = ('id', 'description', 'price', 'link', 'completed', 'project')

# class ReferencePhotoSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ReferencePhoto
#         fields = ('id', 'description', 'photo', 'project')

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'is_superuser', 'first_name', 'last_name')

# class UserSerializerWithToken(serializers.ModelSerializer):

#     token = serializers.SerializerMethodField()
#     password = serializers.CharField(write_only=True)

#     def get_token(self, obj):
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

#         payload = jwt_payload_handler(obj)
#         token = jwt_encode_handler(payload)
#         return token

#     def create(self, validated_data):
#         user = User.objects.create(
#             username = validated_data['username'],
#             first_name = validated_data['first_name'],
#             last_name = validated_data['last_name']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
#         # password = validated_data.pop('password', None)
#         # instance = self.Meta.model(**validated_data)
#         # if password is not None:
#         #     instance.set_password(password)
#         # instance.save()
#         # return instance

#     class Meta:
#         model = User
#         fields = ('token', 'username', 'password', 'first_name', 'last_name')
