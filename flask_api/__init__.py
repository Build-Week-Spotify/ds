import os
from dotenv import load_dotenv
from flask import Flask
import psycopg2
from flask_cors import CORS

from flask_api.routes.spotify_routes import spotify_routes



def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(spotify_routes)

    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
