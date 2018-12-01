from flask import Flask, jsonify, render_template
from mongoengine import connect

from web.modules.auth.Views import authBlueprint
from web.modules.tasks.Views import tasksBlueprint

from web import config as config

app = Flask(__name__.split('.')[0], static_folder=config.STATIC_PATH, template_folder=config.TEMPLATES_PATH)

app.config.from_pyfile('./config.py')

# Mongo connection
connect(**config.buildMongoConnectionArgs())

app.register_blueprint(authBlueprint, url_prefix='/auth')
app.register_blueprint(tasksBlueprint, url_prefix='/tasks')


@app.route('/', methods=['GET'])
def home():
    return render_template('tasks.html')


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)