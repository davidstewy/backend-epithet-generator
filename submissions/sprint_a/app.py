from sprint_a import app
import flask
from .helpers import EpithetGenerator

json_path = '../../resources/data.json'


@app.route('/')
def generate_epithets():
    return flask.jsonify(EpithetGenerator.create_insult(json_path))


@app.route('/epithets/<int:quantity>')
def epithets_quantity(quantity):
    quantity_list = []
    for i in range(quantity):
        quantity_list.append(EpithetGenerator.create_insult(json_path))
    return flask.jsonify(quantity_list)


@app.route('/vocabulary')
def vocabulary():
    return flask.jsonify(EpithetGenerator.all_vocab(json_path))


@app.route('/unleash_nemesis_rant')
def nemesis_rant():
    return flask.jsonify(EpithetGenerator.nemesis_rant(json_path))
