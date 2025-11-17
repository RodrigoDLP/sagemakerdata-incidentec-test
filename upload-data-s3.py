import boto3


def lambda_handler(event, context):
    s3 = boto3.client("s3")
    bucket_name = "sagemakerdata-incidentec-test"
    object_name = "train/incidents_model.csv"
    s3.upload_file("incidents_model.csv", bucket_name, object_name)
    print("Archivo subido a s3 exitosamente")
