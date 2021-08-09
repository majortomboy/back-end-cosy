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
from django.conf.urls.static import static
from rest_framework import routers
from cosyapp import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
# from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
# from cosyapp.views import UploadList

# router = routers.DefaultRouter()
# router.register(r'projects', views.ProjectView, 'cosyapp')
# router.register(r'parts', views.PartView, 'cosyapp')
# router.register(r'tasks', views.TaskView, 'cosyapp')
# router.register(r'uploads', views.ProjectView, 'cosyapp')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('', views.home, name='home'),
    # path('projects/', views.project_list),
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('projects/<int:pk>/parts/', views.ProjectPartsList.as_view()),
    path('projects/<int:pk>/tobuyitems/', views.ProjectToBuyList.as_view()),
    path('parts/<int:pk>/tasks/', views.PartTasksList.as_view()),
    path('parts/', views.PartList.as_view()),
    path('tasks/', views.TaskList.as_view()),
    path('parts/<int:pk>/', views.PartDetail.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('tobuyitems/<int:pk>/', views.ToBuyListDetail.as_view()),
    path('tobuyitems/', views.ToBuyList.as_view()),
    # path('token-auth/', obtain_jwt_token),
    # path('current_user/', views.current_user),
    # path('users/create/', views.CreateUserView.as_view()),
    path('user/register/', views.UserCreate.as_view(), name="create_user"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair')

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
