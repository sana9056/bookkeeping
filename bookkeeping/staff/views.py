from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Staff
from .serializers import StaffSerializer


class ProjectPagination(PageNumberPagination):
    page_size = 10


class StaffViewSet(ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all().order_by("post")
    pagination_class = ProjectPagination
    permission_classes = [IsAdminUser]
