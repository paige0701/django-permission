from enum import Enum


class BasePermissionEnum(Enum):
    @property
    def codename(self):
        return self.value.split('.')[1]


class AccountPermissions(BasePermissionEnum):
    MANAGE_USERS = 'account.manage_users'
    MANAGE_STAFF = 'account.manage_staff'


class KnowledgePermissions(BasePermissionEnum):
    pass