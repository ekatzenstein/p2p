"""Flask view functions for the dataframe resource endpoint."""
import os

from flask import (Blueprint, request, current_app)
from flask_apispec import use_kwargs, marshal_with, doc
from minio import Minio
from minio.error import (BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

from models import db, Dataframe
from .schemas import DataframeSchema
from utils import hexdigest

DATAFRAME = Blueprint('dataframe', __name__)


@DATAFRAME.route('/', methods=['GET'])
@marshal_with(DataframeSchema(many=True), 200)
def get_dataframes():
    return Dataframe.query.all()


@DATAFRAME.route('/', methods=['POST'])
@use_kwargs(DataframeSchema(), locations=('json',))
@marshal_with(DataframeSchema(many=False), 200)
def create_dataframe():
    new_dataframe = Dataframe()
    db.session.add(new_dataframe)
    db.session.commit()
    return new_dataframe


@DATAFRAME.route('/<int:dataframe_id>', methods=['GET'])
@marshal_with(DataframeSchema(many=False), 200)
def get_dataframe(dataframe_id):
    return Dataframe.query.get(dataframe_id)


def _allowed_file(filename):
    return True


def _secure_filename(filename, dataframe_id):
    return f'dataframe_{dataframe_id}.csv'


@DATAFRAME.route('/<int:dataframe_id>', methods=['POST'])
def create_dataframe_content(dataframe_id):
    dataframe = Dataframe.query.get(dataframe_id)
    if not dataframe:
        return 'No dataframe found', 400

    file = request.files.get('file', None)
    if file and _allowed_file(file.filename):
        filename = _secure_filename(file.filename, dataframe_id)
        full_filepath = os.path.join(
            current_app.config['UPLOAD_DIRECTORY'], filename)
        file.save(full_filepath)
        # TODO: move minioClient somewhere global
        minioClient = Minio(current_app.config['MINIO_ENDPOINT'],
                            access_key=current_app.config['MINIO_ACCESS_KEY'],
                            secret_key=current_app.config['MINIO_SECRET_KEY'],
                            secure=False)

        try:
            minioClient.make_bucket("dataframes")
        except BucketAlreadyOwnedByYou:
            pass
        except BucketAlreadyExists:
            pass

        minioClient.fput_object('dataframes', f'dataframe_{dataframe_id}.csv', full_filepath)

        dataframe.url = f"http://{current_app.config['MINIO_DATAFRAME_URL']}{filename}"
        dataframe.digest = hexdigest(full_filepath)
        db.session.commit()

        os.remove(full_filepath)

        return '', 204, {'content-length': 0}

    return 'No file found', 400


@DATAFRAME.route('/<int:dataframe_id>', methods=['DELETE'])
@marshal_with(None, 204, "Dataframe deleted", apply=False)
def delete_page(dataframe_id):
    dataframe = db.session.query(Dataframe).get(dataframe_id)
    print(f'dataframe to delete: {dataframe}')
    db.session.delete(dataframe)
    db.session.commit()
    return '', 204, {'content-length': 0}
