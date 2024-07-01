from django.shortcuts import render
from .models import Course,Students,Teachers
from .serializers import CourseSerializers,TeacherSerializers,StudentsSerializers
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class CourseAPICreateView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class CourseAPIUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class TeachersAPICreateView(ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializers
    permission_classes = [permissions.IsAdminUser]

class TeachersAPIUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializers
    permission_classes = [permissions.IsAdminUser]

class StudentAPICreateView(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializers
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class StudentsAPIUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializers
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
