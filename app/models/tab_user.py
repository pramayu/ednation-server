from uuid import uuid4
from random import randint
from mongoengine import Document, StringField, BooleanField, EmailField, DateTimeField, IntField
from datetime import datetime

class Users(Document):
    strid           = StringField(required=True, unique=True, default=uuid4().hex[:24])
    username        = StringField(required=True, unique=True, min_length=5)
    email           = EmailField(required=True, unique=True)
    phone           = StringField(required=True, unique=True)
    hashpass        = StringField(min_length=8)
    verifystat      = BooleanField(default=False)
    verofycode      = IntField(default=randint(0,999999))
    created_at      = DateTimeField(default=datetime.today())