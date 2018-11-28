import os
from datetime import datetime
from uuid import uuid4

import mongoengine as me
from bson import ObjectId

STATUS_OPTIONS = {
    'TODO': 'To Do',
    'IN_PROGRESS': 'In Progress',
    'DONE': 'Done'
}
class Task(me.Document):
    description = me.StringField(required=True)
    status = me.StringField(required=True, default=STATUS_OPTIONS['TODO'])
    creation_date = me.DateTimeField(required=True, default=datetime.utcnow())
    completion_date = me.DateTimeField(required=False, default=None)
    due_date = me.DateTimeField(required=False, default=None)

    meta = {
        'strict': False,
        'collection': 'tasks'
    }