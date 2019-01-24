"""Flask view functions for the dataframe resource endpoint."""
import os

from flask import (Blueprint, request, current_app)
from flask_apispec import use_kwargs, marshal_with, doc

from models import db, Dataframe
from .schemas import DataframeSchema
from utils import hexdigest, ensure_minio_bucket, upload_minio

DATAFRAME = Blueprint('dataframe', __name__)
BUCKET_NAME = 'dataframes'


@DATAFRAME.route('/', methods=['GET'])
@marshal_with(DataframeSchema(many=True), 200)
def get_dataframes():
    return Dataframe.query.all()


@DATAFRAME.route('/<int:dataframe_id>', methods=['GET'])
@marshal_with(DataframeSchema(many=False), 200)
def get_dataframe(dataframe_id):
    return Dataframe.query.get(dataframe_id)


@DATAFRAME.route('/', methods=['POST'])
@DATAFRAME.route('/<string:dataframe_id>', methods=['PUT'])
@marshal_with(DataframeSchema(many=False), 200)
def create_dataframe_content(dataframe_id=None):
    if dataframe_id is None:
        dataframe = Dataframe()
        db.session.add(dataframe)
        db.session.commit()
        dataframe_id = dataframe.id_
    else:
        dataframe = Dataframe.query.get(int(dataframe_id))
        if not dataframe:
            return 'No dataframe found', 400

    file = request.files.get('file', None)
    if file:
        filename = f'dataframe_{dataframe_id}.csv'
        full_filepath = os.path.join(current_app.config['UPLOAD_DIRECTORY'], filename)
        file.save(full_filepath)

        ensure_minio_bucket(BUCKET_NAME)
        file_url = upload_minio(BUCKET_NAME, full_filepath, filename)
        dataframe.url = file_url
        dataframe.digest = hexdigest(full_filepath)
        db.session.commit()

        os.remove(full_filepath)

        return dataframe

    return 'No file found', 400


@DATAFRAME.route('/<int:dataframe_id>', methods=['DELETE'])
@marshal_with(None, 204, "Dataframe deleted", apply=False)
def delete_page(dataframe_id):
    dataframe = db.session.query(Dataframe).get(dataframe_id)
    print(f'dataframe to delete: {dataframe}')
    db.session.delete(dataframe)
    db.session.commit()
    return '', 204, {'content-length': 0}
