import graphene
from graphene import relay

from graphqls.account.types import CustomUserType

from graphene_django.filter import DjangoFilterConnectionField


class AccountQueries(graphene.ObjectType):

    users = DjangoFilterConnectionField(CustomUserType)
    user = relay.Node.Field(CustomUserType)

