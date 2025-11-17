import sagemaker
from sagemaker.model import Model

session = sagemaker.Session()
role = sagemaker.get_execution_role()

model_uri_tipo = "s3://sagemakerdata-incidentec-test/output/kind/sagemaker-xgboost-2025-11-17-04-01-56-309/output/model.tar.gz"
model_uri_urgencia = "s3://sagemakerdata-incidentec-test/output/urgency/sagemaker-xgboost-2025-11-17-04-07-24-580/output/model.tar.gz"

from sagemaker import image_uris
xgb_image = image_uris.retrieve("xgboost", region=session.boto_region_name, version="1.5-1")

model_tipo = Model(
    image_uri=xgb_image,
    model_data=model_uri_tipo,
    role=role,
    sagemaker_session=session
)

model_urgencia = Model(
    image_uri=xgb_image,
    model_data=model_uri_urgencia,
    role=role,
    sagemaker_session=session
)

predictor_tipo = model_tipo.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large",
    endpoint_name="incidentes-tipo"
)

predictor_urgencia = model_urgencia.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large",
    endpoint_name="incidentes-urgencia"
)