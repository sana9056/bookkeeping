from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from faker import Faker


TEST_USER_QUANTITY = 100
FAKE = Faker()
User = get_user_model()


class Command(BaseCommand):
    help = "Create one superuser, 10 test users"

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Processing... 🚀'))

        # Create superuser
        #User.objects.create_superuser(first_name=settings.FIRST_NAME, middle_name=settings.MIDDLE_NAME,
                                      #last_name=settings.LAST_NAME, date_of_employment=settings.DATE,
                                      #Salary_amount=settings.SALARY1, salary_paid=settings.SALARY2, post=settings.POST)


        # Create test users data
        first_names = [FAKE.unique.first_name() for _ in range(TEST_USER_QUANTITY)]
        middle_names = [FAKE.unique.last_name() for _ in range(TEST_USER_QUANTITY)]
        last_names = [FAKE.unique.email() for _ in range(TEST_USER_QUANTITY)]
        date_of_employments = [FAKE.unique.password() for _ in range(TEST_USER_QUANTITY)]
        Salary_amounts = [FAKE.unique.password() for _ in range(TEST_USER_QUANTITY)]
        salary_paids = [FAKE.unique.password() for _ in range(TEST_USER_QUANTITY)]
        posts = [FAKE.unique.password() for _ in range(TEST_USER_QUANTITY)]

        # Create test users
        for fname, mname, lname, date, sala1, sala2, post in zip(first_names, middle_names, last_names,
                                                                 date_of_employments, Salary_amounts, salary_paids,
                                                                 posts):
            User.objects.create_user(first_name=fname, middle_name=mname,
                                      last_name=lname, date_of_employment=date,
                                      Salary_amount=sala1, salary_paid=sala2, post=post)

        #self.stdout.write(self.style.SUCCESS(
        #    f'Successfully created 🎉\n'
        #    f'Admin creds:\n  username: {settings.USERNAME}\n  '
        #    f'email: {settings.EMAIL}\n  password: {settings.PASSWORD}'
       # ))
