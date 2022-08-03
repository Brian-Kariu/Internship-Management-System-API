from django.conf.urls import include
from django.urls import path
from internsystem.views import (ApplicationViewSet, JobViewSet,
                                LecturerViewSet, OrganizationViewSet,
                                SessionView, StudentProfileViewSet,
                                StudentViewSet, WhoAmIView, get_csrf,
                                logout_view)
from rest_framework.routers import SimpleRouter

student_router = SimpleRouter()
student_router.register('', StudentViewSet)

studentprofile_router = SimpleRouter()
studentprofile_router.register('', StudentProfileViewSet, basename="StudentProfile")

lecturer_router = SimpleRouter()
lecturer_router.register('', LecturerViewSet)

organization_router = SimpleRouter()
organization_router.register('', OrganizationViewSet)

job_router = SimpleRouter()
job_router.register('', JobViewSet)

Application_router = SimpleRouter()
Application_router.register('', ApplicationViewSet)

internsystem_urls = [
    path('student/', include(student_router.urls)),
    path('studentprofile/', include(studentprofile_router.urls)),
    path('lecturer/', include(lecturer_router.urls)),
    path('organization/', include(organization_router.urls)),
    path('job/', include(job_router.urls)),
    path('application/', include(Application_router.urls)),
    path('csrf/', get_csrf, name='api-csrf'),
    path('logout/', logout_view, name='api-logout'),
    path('session/', SessionView.as_view(), name='api-session'),  # new
    path('whoami/', WhoAmIView.as_view(), name='api-whoami'), 
]
