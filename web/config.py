import os

#   Flask environment variables
DEBUG = os.environ.get('DEBUG', True)
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = os.environ.get('PORT', 5000)

#   URI for aux components
STATIC_PATH = '/static'

#   MongoDB credentials and connection------------------------------------------------------------------
DB_HOST = ''
DB_NAME = ''
DB_USER = ''
DB_PASSWORD = ''

def buildMongoConnectionArgs():
    connData = {
        'db': DB_NAME,
        'host': 'mongodb://{host}:{port}/{db_name}'.format(db_name=DB_NAME, port=DB_PORT, host=DB_HOST),
        'connect': False
    }

    if DB_USER and DB_PASSWORD:
        connData['username'] = DB_USER
        connData['password'] = DB_PASSWORD
        #connData['authentication_source'] = DB_NAME_AUTH

    return connData