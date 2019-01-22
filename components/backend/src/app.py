from flask import Flask

from blueprints import (dataframe, site)


def build_app():
    app = Flask(__name__)
    app.register_blueprint(dataframe.DATAFRAME, url_prefix='/dataframes')
    app.register_blueprint(site.SITE, url_prefix='/sites')
    return app


# run the application
if __name__ == "__main__":
    app = build_app()
    app.run(debug=True, host='0.0.0.0')
