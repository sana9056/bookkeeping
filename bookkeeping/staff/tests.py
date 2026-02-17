from datetime import date

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Staff


class StaffFilterViewSetTests(APITestCase):
    def setUp(self):
        self.admin = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='password123',
        )
        self.client.force_authenticate(user=self.admin)

        Staff.objects.create(
            first_name='Ivan',
            middle_name='Ivanovich',
            last_name='Petrov',
            date_of_employment=date(2023, 1, 1),
            Salary_amount='5000',
            salary_paid='yes',
            post='0',
        )
        Staff.objects.create(
            first_name='Anna',
            middle_name='Sergeevna',
            last_name='Sidorova',
            date_of_employment=date(2024, 5, 10),
            Salary_amount='1500',
            salary_paid='no',
            post=Staff.EMPLOYEE_LEVEL,
        )

    def test_filter_endpoint_defaults_to_employee_level(self):
        response = self.client.get('/api/filter/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['post'], Staff.EMPLOYEE_LEVEL)

    def test_filter_endpoint_accepts_post_query_parameter(self):
        response = self.client.get('/api/filter/?post=0')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['post'], '0')
