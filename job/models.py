from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    employee_count = models.IntegerField(blank=True, null=True)
    logo = models.CharField(max_length=128, blank=True)


class Specialty(models.Model):
    code = models.CharField(max_length=128, default=None, null=True)
    title = models.CharField(max_length=128, default=None, null=True)


class Vacancy(models.Model):
    title = models.CharField(max_length=128)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=128, blank=True)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
