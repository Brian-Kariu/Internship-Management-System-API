from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django_filters.rest_framework import DjangoFilterBackend
from internsystem.models import Job, Lecturer, Organization, Student
from internsystem.serializers import (JobSerializer, LecturerSerializer,
                                      OrganizationSerializer,
                                      StudentSerializer)
from rest_framework import filters
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.decorators import api_view
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

@api_view(['POST'])
def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("student/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return JsonResponse({'detail': 'Successfully logged in.'})


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'})
