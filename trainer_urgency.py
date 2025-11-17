import sagemaker
import boto3
from sagemaker import image_uris

session = sagemaker.Session()
role = sagemaker.get_execution_role()

xgb_image = image_uris.retrieve("xgboost", region=session.boto_region_name, version="1.5-1")

xgb = sagemaker.estimator.Estimator(
    image_uri=xgb_image,
    role=role,
    instance_count=1,
    instance_type="ml.t3.large",
    output_path="s3://sagemakerdata-incidentec-test/output/urgency",
    sagemaker_session=session,
)

xgb.set_hyperparameters(
    objective="multi:softmax",
    num_class=3,
    num_round=100
)

xgb.fit({
    "train": "s3://sagemakerdata-incidentec-test/train/urgency",
    "validation": "s3://sagemakerdata-incidentec-test/validation/urgency"
})
