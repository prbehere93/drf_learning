from rest_framework import permissions
from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin(): #the idea here is that this mixin can be used by the views directly
    permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission] #instead of defining perm classes each time
    
class UserQuerySetMixin():
    """
    Mixin to get a queryset which only has the objects which belong to the logged in User
    Can also be customized to a certain extend by overriding the 'user_field' (i.e. you can use any lookup field that you want)
    """
    user_field='user'
    
    def get_queryset(self, *args, **kwargs):
        lookup_data={}
        lookup_data[self.user_field]=self.request.user
        qs=super().get_queryset(*args, **kwargs)
        if self.request.user.is_superuser: #if user is a superuser then he can view everything
            return qs
        return qs.filter(**lookup_data)