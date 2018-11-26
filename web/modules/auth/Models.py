import mongoengine as me
from datetime import datetime


class User(me.Document):
    name = me.StringField(required=True)
    email = me.StringField(required=True)
    registration_date = me.DateTimeField(required=False, default=None)
    company = me.StringField(required=False, default=None)
