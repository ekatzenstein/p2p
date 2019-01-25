import os

from blueprints import (dataframe, page)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models.models import db

def build_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:////{os.environ.get('SQLLITE_DIR', '/tmp')}/p2p.db"
    # TODO: externalize these parameters
    app.config['UPLOAD_DIRECTORY'] = '/tmp'
    app.config['MINIO_ENDPOINT'] = 'compose-minio:9000'
    app.config['MINIO_ACCESS_KEY'] = 'minio'
    app.config['MINIO_SECRET_KEY'] = 'minio123'
    app.config['MINIO_STORAGE_URL'] = 'localhost/file/'

    app.register_blueprint(dataframe.DATAFRAME, url_prefix='/dataframes')
    app.register_blueprint(page.PAGE, url_prefix='/pages')

    return app


# run the application
if __name__ == "__main__":
    app = build_app()
    db.init_app(app)

    # TODO: This belongs somewhere else?
    with app.app_context():
        db.create_all()

    app.run(debug=True, host='0.0.0.0')

