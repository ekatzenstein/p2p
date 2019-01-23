"""Flask view functions for the dataframe resource endpoint."""
from flask import (Blueprint, jsonify)

from flask_apispec import use_kwargs, marshal_with, doc

from models import db, Dataframe
from .schemas import DataframeSchema

DATAFRAME = Blueprint('dataframe', __name__)


@DATAFRAME.route('/', methods=['GET'])
@marshal_with(DataframeSchema(many=True), 200)
def get_dataframes():
    return Dataframe.query.all()


@DATAFRAME.route('/', methods=['POST'])
@use_kwargs(DataframeSchema(), locations=('json',))
@marshal_with(DataframeSchema(many=False), 200)
def create_dataframe(digest, url):
    # TODO: How are we actually uploading dataframes? multipart csv upload?
    new_dataframe = Dataframe(digest=digest, url=url)
    db.session.add(new_dataframe)
    db.session.commit()
    return new_dataframe


@DATAFRAME.route('/<int:dataframe_id>', methods=['GET'])
@marshal_with(DataframeSchema(many=False), 200)
def get_dataframe(dataframe_id):
    return Dataframe.query.get(dataframe_id)


@DATAFRAME.route('/<int:dataframe_id>', methods=['DELETE'])
@marshal_with(None, 204, "Dataframe deleted", apply=False)
def delete_page(dataframe_id):
    dataframe = db.session.query(Dataframe).get(dataframe_id)
    print(f'dataframe to delete: {dataframe}')
    db.session.delete(dataframe)
    db.session.commit()
    return '', 204, {'content-length': 0}
