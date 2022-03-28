from django.core.management import BaseCommand

from staff.models import Staff


class Command(BaseCommand):

    def handle(self, *args, **options):
        Staff.objects.all().delete()
        Staff.objects.create_user(first_name='Sala', middle_name='Sala', last_name='Sala', date_of_employment='123',
                                   Salary_amount='123', salary_paid='123', post='123',)
