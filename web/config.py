import os

#   Flask environment variables------------------------------------------------------------------------
DEBUG = os.environ.get('DEBUG', True)
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = os.environ.get('PORT', 5000)

#   URI for aux components
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = ROOT_DIR + '/web/static'
TEMPLATES_PATH = '/web/templates'

#   MongoDB credentials and connection------------------------------------------------------------------
DB_HOST = 'ds139781.mlab.com'
DB_NAME = 'dailytasker'
DB_USER = 'admin'
DB_PASSWORD = 'admin1234'
DB_PORT = 39781

#   Security--------------------------------------------------------------------------------------------
SECRET_JWT = "H.'R<_X4=^69Mvyr"


def buildMongoConnectionArgs():

    connData = {
        'db': DB_NAME,
        'host': 'mongodb://{host}:{port}/{db_name}'.format(db_name=DB_NAME, port=DB_PORT, host=DB_HOST),
        'connect': False
    }

    if DB_USER and DB_PASSWORD:
        connData['username'] = DB_USER
        connData['password'] = DB_PASSWORD

    return connData
