from rest_framework.viewsets import ModelViewSet
from .serializers import StaffSerializer
from .models import Staff
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser


class ProjectPagination(PageNumberPagination):
    page_size = 10


class StaffViewSet(ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    pagination_class = ProjectPagination
    permission_classes = [IsAdminUser]

class StaffFilterViewSet(StaffViewSet):

    def get_queryset(self):
        queryset = Staff.objects.all()
        queryset = queryset.filter(post="4")
        return queryset
