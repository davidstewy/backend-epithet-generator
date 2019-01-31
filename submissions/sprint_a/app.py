from sprint_a import configure_app
import flask

app = configure_app()


@app.route('/')
def generate_epithets():
    return flask.jsonify({"epithets": []})


@app.route('/vocabulary')
def vocabulary():
    return flask.jsonify({"vocabulary": {}})
