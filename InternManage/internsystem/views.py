from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from internsystem.models import Job, Lecturer, Organization, Student
from internsystem.serializers import (JobSerializer, LecturerSerializer,
                                      OrganizationSerializer,
                                      StudentSerializer)
from rest_framework import filters
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class StudentViewSet(ModelViewSet):
    model = Student
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['field_of_specialization', 'organization']
    search_fields = ['first_name', 'field_of_specialization', 'organization']

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

class LecturerViewSet(ModelViewSet):
    model = Lecturer
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['field_of_specialization', 'organization']
    search_fields = ['first_name', 'field_of_specialization', 'organization']


class OrganizationViewSet(ModelViewSet):
    model = Organization
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['name', 'type']
    search_fields = ['name', 'type']


class JobViewSet(ModelViewSet):
    model = Job
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['title', 'employment_type']
    search_fields = ['title', 'employment_type', 'workplace']
