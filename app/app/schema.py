import graphene
from tracks import schema as tracks_schema
from users import schema as users_schema


class Query(tracks_schema.Query, graphene.ObjectType):
    pass


class Mutation(users_schema.Mutation, tracks_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
