from rest_framework.permissions import BasePermission
from api.models import Comment


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_comment = view.kwargs['pk']
            comment = Comment.objects.get(pk=id_comment)
            if request.user.pk == comment.user_id:
                return True
            return False
