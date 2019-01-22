from flask import (Blueprint, jsonify)

DATAFRAME = Blueprint('dataframe', __name__)

_dataframes = [
    {
        'id': '0',
        'digest': 'abc',
        'url': '/myurl'
    },
    {
        'id': '1',
        'digest': 'abc',
        'url': '/myurl'
    }
]


@DATAFRAME.route('/', methods=['GET'])
def list_dataframes():
    dataframes = _dataframes
    return jsonify(dataframes)


@DATAFRAME.route('/<int:dataframe_id>', methods=['GET'])
def get_dataframe(dataframe_id):
    dataframe = _dataframes[dataframe_id]
    return jsonify(dataframe)
