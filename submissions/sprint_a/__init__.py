def configure_app():
    import os
    import dotenv
    import flask

    PROJECT_ROOT = os.path.dirname((__file__))
    env_path = os.path.join(PROJECT_ROOT, '.env')
    dotenv.load_dotenv(env_path)

    app = flask.Flask(__name__)

    return app


app = configure_app()
