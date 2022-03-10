from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)
    
    # def has_permission(self, request, view):
    #     user=request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("products.add_products"): #The format for perm - "appname.verb_modelname"
    #             return True
    #         if user.has_perm("products.change_products"):
    #             return True
    #         if user.has_perm("products.delete_products"):
    #             return True
    #         if user.has_perm("products.view_products"):
    #             return True
    #         return False
    #     return False
    
    # def has_object_permission(self, request, view, obj):
    #     return super().has_object_permission(request, view, obj)