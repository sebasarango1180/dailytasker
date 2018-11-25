from flask import Blueprint, request, jsonify
from http import HTTPStatus
import mongoengine
import logging

import config as config
from .utils import check_hashed_password, encoded_jwt, decode_cookie

authBlueprint = Blueprint('auth', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@authBlueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json() if request.get_json() else dict()
    user = data.get('user', '')
    password = data.get('password', '')

    result_user = users_ao.users.find_one({'email': user})

    if result_user:
        if check_hashed_password(password, result_user['password']):
            if not result_user['confirmed']:
                return jsonify({'login': False, 'msg': 'User not confirmed'})

            return jsonify({'login': True, 'token': encoded_jwt(result_user), 'uid': str(result_user['_id']),
                            'email': result_user['email'], 'currentPlanLevel': l_p['currentPlanLevel'],
                            'names': result_user['name'] + ' ' + result_user['lastname']})

    return jsonify({'login': False, 'msg': 'wrong username or password'}), HTTPStatus.BAD_REQUEST
