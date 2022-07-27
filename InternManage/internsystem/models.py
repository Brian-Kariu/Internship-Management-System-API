import uuid

from django.contrib.auth import get_user_model
from django.db import models
from internsystem.choices import (Employment_Type, Organization,
                                  Specialization, Workplace)

User = get_user_model()


class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    field_of_specialization = models.CharField(
        max_length=30, choices=Specialization.CHOICES)
    organization = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_user")

    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "Students"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


class Lecturer(User):
    lecturer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    field_of_specialization = models.CharField(
        max_length=30, choices=Specialization.CHOICES)
    organization = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lecturer_user")

    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "Lecturers"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Organization(models.Model):
    organization_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=Organization.CHOICES)


class Job(models.Model):
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    workplace = models.CharField(max_length=30, choices=Workplace.CHOICES)
    location = models.CharField(max_length=255)
    employment_type = models.CharField(
        max_length=50, choices=Employment_Type.CHOICES)

class Application(models.Model):
    application_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="application_student")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="application_job")
    approved = models.BooleanField()
