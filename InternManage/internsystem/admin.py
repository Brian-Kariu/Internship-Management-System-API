from django.contrib import admin

from .models import Job, Lecturer, Organization, Student

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Organization)
admin.site.register(Job)
