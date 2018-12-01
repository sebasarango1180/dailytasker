from flask import jsonify, Blueprint, request, render_template, g
from http import HTTPStatus
from bson import ObjectId
import logging
from datetime import datetime

from web.modules.tasks.Models import Task

tasksBlueprint = Blueprint('tasks', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@tasksBlueprint.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
@tasksBlueprint.route('/<task_id>', methods=['PUT', 'DELETE'])
def process_tasks(task_id=None):
    """
    Performs RESTful operations over Task objects.

    GET: retrieves a list of current tasks.
    POST: Creates a new task instance.
    PUT: Updates an existing task - input: (task_id, **kwargs)
    DELETE: Deletes an existing instance of Task. - input: (task_id)

    """

    if request.method == 'GET':
        
        try:
        
                task_list = list()
                for task in Task.objects().order_by('creation_date'):
                        task_data = {
                                'id': str(task.id),
                                'description': task.description,
                                'status': task.status,
                                'due_date': str(task.due_date),
                                'creation_date': str(task.creation_date),
                                'completion_date': str(task.completion_date)
                        }
                        task_list.append(task_data)

                return jsonify({'list':task_list})

        except Exception as e:
                return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


    elif request.method == 'POST':

        data = request.get_json() if request.get_json() else dict()

        try:

                if type(data.get('due_date')) == str:
                        data['due_date'] == datetime.strptime(data.get('due_date'), '%Y-%m-%d')

                if not data.get('description'):
                        return jsonify({'error': 'No description added'}), HTTPStatus.BAD_REQUEST

                task = Task(**data).save()

                return jsonify({'task_id': str(task.id)}), HTTPStatus.CREATED

        except Exception as e:
                return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


    elif request.method == 'PUT':

        data = request.get_json() if request.get_json() else dict()
        t_id = task_id if task_id else request.get_json().get('task_id')

        try:

                task = Task.objects(id=ObjectId(t_id)).modify(set__status= data.get('status'), upsert=False)

                if task:
                        return jsonify({'task_id': str(t_id)}), HTTPStatus.OK
                else:
                        return jsonify({'error': 'The document could not be edited as it was not found in the DB'}), HTTPStatus.BAD_REQUEST

        except Exception as e:
                return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


    elif request.method == 'DELETE':

        data = request.get_json() if request.get_json() else dict()
        t_id = task_id if task_id else request.get_json().get('task_id')

        try:
                task = Task.objects(id=ObjectId(t_id)).first()
                task.delete()
                return jsonify({'task_id': t_id}), 204

        except Exception as e:
                return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST
