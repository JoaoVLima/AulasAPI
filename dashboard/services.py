"""
Services
- This file contains service classes that implement business logic for the app.
- Services handle complex operations and validations that don't belong in views or models.
- They act as an intermediate layer between views and database queries.
"""
from core.middleware import get_current_user
from core.services import BaseService
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import NotFound, PermissionDenied
from utils.decorators import Response
from .queries import DashboardQuery


class DashboardService(BaseService):
    def __init__(self):
        super().__init__(query=DashboardQuery)

    @Response(success_message=_('Successfully retrieved dashboard data'),
              error_message=_('Failed to get dashboard data'))
    def get_dashboard_data(self, group, year: int, month: int = None, day: int = None):
        """Get dashboard data if user has permission."""
        user = get_current_user()

        # Check if user has permission to view this dashboards
        if not user.has_perm('dashboard.view_dashboard'):
            raise PermissionDenied(_('User does not have permission to view dashboards'))
        # Check if user has permission to view this group's dashboard
        if not user.groups.filter(id=group).exists():
            raise PermissionDenied(_('User does not have permission to access this group\'s dashboard'))

        dashboard_data = self.query.get_object_json(group, year, month, day)
        if not dashboard_data:
            raise NotFound(_('No dashboard data found'))

        return dashboard_data

