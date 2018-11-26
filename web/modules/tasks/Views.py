from flask import jsonify, Blueprint, request
from http import HTTPStatus
from bson import ObjectId
import logging

tasksBlueprint = Blueprint('tasks', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@tasksBlueprint.route('/list', methods=['GET'])
def get_all():
    """
    Retrieves an array containing all the tasks
    """
    #   Eventually to be replaced in favor of DB
    task1 = {'id': 1234, 'description': 'Create frontend', 'status': 'to do', 'creation_date': '20-11-2018', 'due_date': '02-12-2018'}
    task2 = {'id': 5678, 'description': 'Create backend', 'status': 'in process', 'creation_date': '20-11-2018', 'due_date': '02-12-2018'}
    tasks = [task1, task2]

    return jsonify({'tasks': tasks}), HTTPStatus.OK

@tasksBlueprint.route('/create-task', methods=['POST'])
def create_task():
    """
    Creates a task
    """

    if request.method == 'POST':
        data = request.get_json() if request.get_json() else dict()

        task = data #   Eventually stored in DB

        return jsonify({'task_id': task.id}), HTTPStatus.CREATED

@tasksBlueprint.route('/edit-task', methods=['POST'])
def edit_task():
    """
    Edits a task
    """

    if request.method == 'POST':
        data = request.get_json() if request.get_json() else dict()

        task = data #   Eventually stored in DB

        return jsonify({'task_id': task.id}), HTTPStatus.CREATED


@tasksBlueprint.route('/delete-task', methods=['POST'])
def delete_task():
    """
    Deletes a task
    """

    if request.method == 'POST':
        data = request.get_json() if request.get_json() else dict()

        task = data.get('id') #   Eventually deleted in DB

        return jsonify({'task_id': task.id}), HTTPStatus.CREATED
