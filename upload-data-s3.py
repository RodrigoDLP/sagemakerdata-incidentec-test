import boto3


def lambda_handler(event, context):
    s3 = boto3.client("s3")
    bucket = "sagemakerdata-incidentec-test"
    s3.upload_file("incidents_train_tipo.csv", bucket, "train/urgency/incidents_train_urgencia.csv")
    s3.upload_file("incidents_validation_tipo.csv", bucket, "validation/urgency/incidents_validation_urgencia.csv")
    s3.upload_file("incidents_test_tipo.csv", bucket, "test/urgency/incidents_test_urgencia.csv")
    s3.upload_file("incidents_train_urgencia.csv", bucket, "train/urgency/incidents_train_urgencia.csv")
    s3.upload_file("incidents_validation_urgencia.csv", bucket,
                   "validation/urgency/incidents_validation_urgencia.csv")
    s3.upload_file("incidents_test_urgencia.csv", bucket, "test/urgency/incidents_test_urgencia.csv")
    return {"statusCode": 200, "response": "Archivos subidos a s3 exitosamente"}
