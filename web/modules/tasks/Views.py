from flask import jsonify, Blueprint, request, render_template, g
from http import HTTPStatus
from bson import ObjectId
import logging
from datetime import datetime

from web.modules.tasks.Models import Task

tasksBlueprint = Blueprint('tasks', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@tasksBlueprint.route('/', methods=['GET'])
def get_all():
    """
    Retrieves an array containing all the tasks
    """
    task_list = list()
    for task in Task.objects:
            task_data = {
                    'id': task.id,
                    'description': task.description,
                    'status': task.status,
                    'due_date': task.due_date,
                    'creation_date': task.creation_date,
                    'completion_date': task.completion_date
            }
            task_list.append(task_data)

    return jsonify({'list':task_list})

@tasksBlueprint.route('/', methods=['POST'])
def create_task():
    """
    Creates a task
    """

    if request.method == 'POST':
        data = request.get_json() if request.get_json() else dict()

        if type(data.get('due_date')) == str:
                data['due_date'] == datetime.strptime(data.get('due_date'), '%Y-%m-%d')

        if not data.get('description'):
                return jsonify({'error': 'No description added'}), HTTPStatus.BAD_REQUEST

        task = Task(**data).save()

        return jsonify({'task_id': str(task.id)}), HTTPStatus.CREATED

@tasksBlueprint.route('/edit-task', methods=['POST'])
def edit_task():
    """
    Edits a task
    """

    if request.method == 'POST':
        data = request.get_json() if request.get_json() else dict()

        task = data #   Eventually stored in DB

        return jsonify({'task_id': task.id}), HTTPStatus.OK


@tasksBlueprint.route('/delete-task', methods=['POST'])
def delete_task():
    """
    Deletes a task
    """

    if request.method == 'POST':
        data = request.get_json() if request.get_json() else dict()

        task = data.get('id') #   Eventually deleted in DB

        return jsonify({'task_id': task.id}), HTTPStatus.OK
