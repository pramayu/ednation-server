from graphene import String, ID, ObjectType, DateTime, Boolean

class UserType(ObjectType):
    id          = ID()
    strid       = String()
    username    = String()
    email       = String()
    phone       = String()
    created_at  = DateTime()


class ServiceResponse(ObjectType):
    status      = Boolean()
    errorpath   = String()
    infopath    = String()