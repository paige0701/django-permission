from enum import Enum


class BasePermissionEnum(Enum):
    @property
    def codename(self):
        return self.value.split('.')[1]


class AccountPermissions(BasePermissionEnum):
    MANAGE_USERS = 'users.manage_users'
    MANAGE_STAFF = 'users.manage_staff'


class KnowledgePermissions(BasePermissionEnum):
    pass