from graphene_federation import build_schema

from graphqls.account.schema import AccountQueries


class Query(
    AccountQueries
):
    pass


schema = build_schema(Query)
