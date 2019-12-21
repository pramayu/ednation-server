from bcrypt import hashpw, gensalt
from mongoengine.queryset.visitor import Q
from graphene import String, ObjectType, Mutation
from app.models.tab_user import Users as UserModel
from app.api.schema.sche_user import UserType, ServiceResponse


class CreateUser(Mutation):
    class Arguments:
        username    = String()
        email       = String()
        phone       = String()
        password    = String()
    
    Output = ServiceResponse

    def mutate(args, info, **kwargs):
        if len(kwargs['username']) != 0 or len(kwargs['email']) != 0 or len(kwargs['phone']) != 0:
            if len(kwargs['password']) < 8:
                return ServiceResponse(status=False, errorpath="create_user", infopath="Password min length 8")
            else:
                user = UserModel.objects(Q(username=kwargs['username']) | Q(email=kwargs['email']) | Q(phone=kwargs['phone']))
                if user:
                    return ServiceResponse(status=False, errorpath="create_user", infopath="Username or email already taken")
                else:
                    encodepass = kwargs['password'].encode('utf-8')
                    hashpass = hashpw(encodepass, gensalt(16))
                    user = UserModel(username=kwargs['username'], email=kwargs['email'], phone=kwargs['phone'], hashpass=hashpass)
                    user.save()
                    if user:
                        return ServiceResponse(status=True)
                    else:
                        return ServiceResponse(status=False, errorpath="create_user", infopath="Something wrong")
        else:
            return ServiceResponse(status=False, errorpath="create_user", infopath="Fields can't be empty")


class CreateUserService(ObjectType):
    createuser = CreateUser.Field()