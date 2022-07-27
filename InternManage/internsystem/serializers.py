from internsystem.models import (Application, Job, Lecturer, Organization,
                                 Student)
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class LecturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecturer
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = "__all__"

class ApplicationSerializer(serializers.ModelSerializer):
    job_description = serializers.SerializerMethodField(read_only=True)
    student_profile = serializers.SerializerMethodField(read_only=True)

    def get_job_description(self, instance):
        res = Job.objects.get(application_job = instance)
        return JobSerializer(res).data

    def get_student_profile(self, instance):
        res = Student.objects.get(application_student = instance)
        return StudentSerializer(res).data
    class Meta:
        model = Application
        fields = ['application_id', 'student', 'job', 'approved', 'job_description', 'student_profile']
        lookup_field = "application_id"
    