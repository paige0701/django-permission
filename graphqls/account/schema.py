import graphene

from users.models import CustomUser
from graphqls.account.types import CustomUserType


class AccountQueries(graphene.ObjectType):

    users = graphene.List(CustomUserType)

    def resolve_users(root, info):
        tmp = CustomUser.objects.all()
        return tmp
