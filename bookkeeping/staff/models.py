from django.db import models


class Staff(models.Model):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_employment = models.DateField()
    Salary_amount = models.CharField(max_length=64)
    salary_paid = models.CharField(max_length=64)
    EMP_LEVELS = (
        ('0', u'Director'),
        ('1', u'Group Leader'),
        ('2', u'Middle manager'),
        ('3', u'Manager'),
        ('4', u'Employee'),
    )
    post = models.CharField(u'Post', max_length=15, choices=EMP_LEVELS, primary_key=True)


class Boss(models.Model):
    BOSS_LEVELS = (
        ('0', u'You BOSS'),
        ('1', u'Director'),
        ('2', u'Group Leader'),
        ('3', u'Middle manager'),
        ('4', u'Manager'),
    )
    boss_name = models.CharField(u'Post', max_length=15, choices=BOSS_LEVELS, default=" ")
    subordinate_level = models.CharField(u'Subordinate', max_length=15, choices=Staff.EMP_LEVELS, primary_key=True)
