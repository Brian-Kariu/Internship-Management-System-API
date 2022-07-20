from django.conf.urls import include
from django.urls import path
from internsystem.views import (JobViewSet, LecturerViewSet,
                                OrganizationViewSet, StudentViewSet)
from rest_framework.routers import SimpleRouter

student_router = SimpleRouter()
student_router.register('', StudentViewSet)

lecturer_router = SimpleRouter()
lecturer_router.register('', LecturerViewSet)

organization_router = SimpleRouter()
organization_router.register('', OrganizationViewSet)

job_router = SimpleRouter()
job_router.register('', JobViewSet)
internsystem_urls = [
    path('student/', include(student_router.urls)),
    path('lecturer/', include(lecturer_router.urls)),
    path('organization/', include(organization_router.urls)),
    path('job/', include(job_router.urls)),
]
