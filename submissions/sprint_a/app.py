from sprint_a import app
import flask
from .helpers import EpithetGenerator

json_path = '../../resources/data.json'


@app.route('/')
def generate_epithets():
    return flask.jsonify(EpithetGenerator.create_insult(json_path))


@app.route('/vocabulary')
def vocabulary():
    return flask.jsonify(EpithetGenerator.all_vocab(json_path))
