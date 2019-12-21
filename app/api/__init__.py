from graphene import ObjectType, Schema

# service
from app.api.services.users.serv_createuser import CreateUserService

# query
from app.api.queries.que_users import UserQuery

class Query(UserQuery, ObjectType):
    pass

class Service(CreateUserService, ObjectType):
    pass

schema = Schema(query=Query, mutation=Service)