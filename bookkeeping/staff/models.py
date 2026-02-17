from django.db import models


class Staff(models.Model):
    EMP_LEVELS = (
        ('0', 'Director'),
        ('1', 'Group Leader'),
        ('2', 'Middle manager'),
        ('3', 'Manager'),
        ('4', 'Employee'),
    )
    EMPLOYEE_LEVEL = '4'

    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_employment = models.DateField()
    Salary_amount = models.CharField(max_length=64)
    salary_paid = models.CharField(max_length=64)
    post = models.CharField('Post', max_length=15, choices=EMP_LEVELS, primary_key=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.get_post_display()})"


class Boss(models.Model):
    BOSS_LEVELS = (
        ('0', 'You BOSS'),
        ('1', 'Director'),
        ('2', 'Group Leader'),
        ('3', 'Middle manager'),
        ('4', 'Manager'),
    )

    boss_name = models.CharField('Post', max_length=15, choices=BOSS_LEVELS, default=' ')
    subordinate_level = models.CharField('Subordinate', max_length=15, choices=Staff.EMP_LEVELS, primary_key=True)

    def __str__(self):
        return f"{self.get_boss_name_display()} -> {self.get_subordinate_level_display()}"
