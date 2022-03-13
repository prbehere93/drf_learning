from rest_framework import permissions
from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin(): #the idea here is that this mixin can be used by the views directly
    permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission] #instead of defining perm classes each time
    