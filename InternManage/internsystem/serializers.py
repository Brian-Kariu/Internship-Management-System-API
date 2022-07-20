from internsystem.models import Job, Lecturer, Organization, Student
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
