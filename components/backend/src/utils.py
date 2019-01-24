from hashlib import md5
from json import dumps

from flask import current_app
from minio import Minio
from minio.error import (BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

POLICY_WORLD_READ = {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Principal": {"AWS": ["*"]}, "Action":["s3:GetBucketLocation", "s3:ListBucket", "s3:ListBucketMultipartUploads"], "Resource":["arn:aws:s3:::dataframes"]}, {
    "Effect": "Allow", "Principal": {"AWS": ["*"]}, "Action":["s3:GetObject", "s3:ListMultipartUploadParts", "s3:PutObject", "s3:AbortMultipartUpload", "s3:DeleteObject"], "Resource":["arn:aws:s3:::dataframes/*"]}]}


def hexdigest(filepath):
    hasher = md5()
    with open(filepath, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

def get_minio_client():
    minioClient = Minio(current_app.config['MINIO_ENDPOINT'],
                        access_key=current_app.config['MINIO_ACCESS_KEY'],
                        secret_key=current_app.config['MINIO_SECRET_KEY'],
                        secure=False)
    return minioClient

def ensure_minio_bucket(bucket_name):
    try:
        minioClient = get_minio_client()
        minioClient.make_bucket(bucket_name)
        minioClient.set_bucket_policy(bucket_name, dumps(POLICY_WORLD_READ))
    except BucketAlreadyOwnedByYou:
        pass
    except BucketAlreadyExists:
        pass

def upload_minio(bucket_name, source_path, destination_name):
    minioClient = get_minio_client()
    minioClient.fput_object(bucket_name, destination_name, source_path)
    return f"http://{current_app.config['MINIO_STORAGE_URL']}{bucket_name}/{destination_name}"
