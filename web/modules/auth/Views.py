from flask import Blueprint, request, jsonify
from http import HTTPStatus
import mongoengine
import logging

from web import config
from web.modules.auth.Models import User
from .utils import check_hashed_password, encoded_jwt

authBlueprint = Blueprint('auth', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@authBlueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json() if request.get_json() else dict()
    user = data.get('user', '')
    password = data.get('password', '')

    result_user = User.objects({'email': user}).first()

    if result_user:
        if check_hashed_password(password, result_user['password']):
            if not result_user['confirmed']:
                return jsonify({'login': False, 'msg': 'User not confirmed'})

            return jsonify({'login': True, 'token': encoded_jwt(result_user), 'uid': str(result_user['_id']),
                            'email': result_user['email']})

    "return jsonify({'login': False, 'msg': 'wrong username or password'}), HTTPStatus.BAD_REQUEST"""

    return jsonify({'login': True})
