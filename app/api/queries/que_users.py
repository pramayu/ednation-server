from graphene import ObjectType, String, List
from app.api.schema.sche_user import UserType

class UserQuery(ObjectType):
    users = List(UserType)

    def resolve_users(parent, info):
        return "hello world"