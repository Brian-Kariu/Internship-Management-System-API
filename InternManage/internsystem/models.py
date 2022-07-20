from django.contrib.auth import get_user_model
from django.db import models
from internsystem.choices import (Employment_Type, Organization,
                                  Specialization, Workplace)

User = get_user_model()


class Student(User):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    field_of_specialization = models.CharField(
        max_length=30, choices=Specialization.CHOICES)
    organization = models.CharField(max_length=30)

    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "Profiles"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Lecturer(User):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    field_of_specialization = models.CharField(
        max_length=30, choices=Specialization.CHOICES)
    organization = models.CharField(max_length=30)

    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "Profiles"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Organization(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=Organization.CHOICES)


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    workplace = models.CharField(max_length=30, choices=Workplace.CHOICES)
    location = models.CharField(max_length=255)
    employment_type = models.CharField(
        max_length=50, choices=Employment_Type.CHOICES)
