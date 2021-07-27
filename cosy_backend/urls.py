"""cosy_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cosyapp import views
# from cosyapp.views import UploadList

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectView, 'cosyapp')
router.register(r'parts', views.PartView, 'cosyapp')
router.register(r'tasks', views.TaskView, 'cosyapp')
router.register(r'uploads', views.ProjectView, 'cosyapp')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('media/', include(router.urls))
    # path('uploads/', UploadList.as_view()),
]
