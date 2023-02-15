import graphene
import banksAPI.schema

class Query(banksAPI.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)