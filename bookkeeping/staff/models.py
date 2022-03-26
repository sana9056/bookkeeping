from django.db import models


class Staff(models.Model):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    post = models.CharField(max_length=64)
    date_of_employment = models.PositiveIntegerField()
    Salary_amount = models.CharField(max_length=64)
    salary_paid = models.CharField(max_length=64)
