from .models import Staff
from .views import StaffViewSet


class StaffFilterViewSet(StaffViewSet):
    """Filter staff by hierarchy level.

    Defaults to employee level if query parameter is not passed.
    """

    def get_queryset(self):
        post = self.request.query_params.get("post", Staff.EMPLOYEE_LEVEL)
        return Staff.objects.filter(post=post).order_by("post")
