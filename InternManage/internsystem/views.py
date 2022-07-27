from django.contrib.auth import logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django_filters.rest_framework import DjangoFilterBackend
from internsystem.models import (Application, Job, Lecturer, Organization,
                                 Student)
from internsystem.serializers import (ApplicationSerializer, JobSerializer,
                                      LecturerSerializer,
                                      OrganizationSerializer,
                                      StudentSerializer)
from rest_framework import filters
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.decorators import action
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class StudentViewSet(ModelViewSet):
    model = Student
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['field_of_specialization', 'organization']
    search_fields = ['first_name', 'field_of_specialization', 'organization']


class LecturerViewSet(ModelViewSet):
    model = Lecturer
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['title', 'employment_type']
    search_fields = ['title', 'employment_type', 'workplace']

class ApplicationViewSet(ModelViewSet):
    model = Application
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'application_id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['application_id', 'approved']
    search_fields = ['application_id', 'approved', 'student_profile']

class SessionView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({'isAuthenticated': True})


class WhoAmIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({'username': request.user.username})


@ensure_csrf_cookie
def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'})
