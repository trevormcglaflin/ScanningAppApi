from rest_framework import permissions
from .models import Company

class CompanyBelongsToUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return not Company.objects.filter(user_id=request.user.id).filter(id=view.kwargs['company_pk']).count() == 0
            