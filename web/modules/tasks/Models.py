import mongoengine as me
from datetime import datetime


class Task(me.Document):
    user_id = me.ObjectIdField(required=True)
    description = me.StringField(required=True)
    status = me.StringField(required=True)
    creation_date = me.DateTimeField(required=True, default=datetime.utcnow())
    completion_date = me.DateTimeField(required=False, default=None)
    due_date = me.DateTimeField(required=False, default=None)