import graphene
from graphene_django import DjangoObjectType
from graphene_federation import key

from users.models import CustomUser


@key(fields="id")
@key(fields="email")
class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        interfaces = (graphene.relay.Node, )
        filter_fields = ["id", "email"]
