"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from education.views import (CourseAPICreateView,CourseAPIUpdateDeleteView,TeachersAPICreateView,
                             TeachersAPIUpdateDeleteView,StudentAPICreateView,StudentsAPIUpdateDeleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/course/',CourseAPICreateView.as_view()),
    path('api/v1/teachers/',TeachersAPICreateView.as_view()),
    path('api/v1/students/',StudentAPICreateView.as_view()),
    path('api/v1/course/<int:pk>/',CourseAPIUpdateDeleteView.as_view()),
    path('api/v1/teachers/<int:pk>/',TeachersAPIUpdateDeleteView.as_view()),
    path('api/v1/students/<int:pk>/',StudentsAPIUpdateDeleteView.as_view()),
    path('api-auth/',include('rest_framework.urls')),
]
