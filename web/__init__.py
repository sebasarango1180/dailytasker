from flask import Flask, jsonify
from mongoengine import connect

from web.modules.auth.Views import authBlueprint
from web.modules.tasks.Views import tasksBlueprint

from web import config

app = Flask(__name__, static_folder=config.STATIC_PATH, templates_folder=config.TEMPLATES_PATH)

app.config.from_object('web.config')

# Mongo connection
connect(**config.buildMongoConnectionArgs())

app.register_blueprint(authBlueprint, url_prefix='/auth')
app.register_blueprint(tasksBlueprint, url_prefix='/tasks')


@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'active'})


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)