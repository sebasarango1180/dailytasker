import jwt
import datetime
from passlib.hash import pbkdf2_sha512

from web import config

# decode cookie
import hashlib
from itsdangerous import URLSafeTimedSerializer
from flask.sessions import TaggedJSONSerializer


def check_hashed_password(password, hashed_password):
    return pbkdf2_sha512.verify(password, hashed_password)


def encoded_jwt(user):
    return jwt.encode(
        {
            '_id': str(user['_id']),
            'name': user['name'],
            'email': user['email'],
            'token_expiration': datetime.datetime.utcnow() + datetime.timedelta(days=31),  # expires 31 day
            'registration_date': user['registration_date'],
            'company_name': user['company']
        },
        config.SECRET_JWT,
        algorithm='HS256'
    ).decode('utf-8')


def check_token(token):
    """ Validate token """
    try:
        return jwt.decode(
            token, config.SECRET_JWT,
            algorithms = ['HS512', 'HS256']
        )

    except:
        return False # expired token
