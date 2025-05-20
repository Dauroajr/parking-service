from rest_framework import permissions


# class IsVehicleOrRecordOwner(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         user = request.user

#         if hasattr(obj, 'owner'):
#             return obj.owner and obj.owner.user == user

#         if hasattr(obj, 'vehicle') and hasattr(obj.vehicle, 'owner'):
#             return obj.vehicle.owner and obj.vehicle.owner.user == user

#         return False


class IsVehicleOrRecordOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        has_permissions = obj.owner.user == request.user
        return has_permissions
