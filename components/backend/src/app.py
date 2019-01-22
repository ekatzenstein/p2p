from blueprints import (dataframe, site)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models.models import db

def build_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	app.register_blueprint(dataframe.DATAFRAME, url_prefix='/dataframes')
	app.register_blueprint(site.SITE, url_prefix='/sites')

	return app


# run the application
if __name__ == "__main__":
    app = build_app()
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0')
