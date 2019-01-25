from blueprints import (dataframe, page)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models.models import db

def build_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # TODO: Connect to actual DB through variables
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////sqllite-db/test.db'
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

