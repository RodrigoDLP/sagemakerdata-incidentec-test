import sagemaker
from sagemaker.model import Model

session = sagemaker.Session()
role = "arn:aws:455247111280:role/LabRole"

# Artefactos del modelo entrenado (estos se generan al correr .fit())
model_uri_tipo = "s3://sagemakerdata-incidentec-test/output/tipo/output/model.tar.gz"
model_uri_urgencia = "s3://sagemakerdata-incidentec-test/output/urgencia/output/model.tar.gz"

# Imagen de XGBoost
from sagemaker import image_uris
xgb_image = image_uris.retrieve("xgboost", region=session.boto_region_name, version="1.5-1")

# Modelo de tipo
model_tipo = Model(
    image_uri=xgb_image,
    model_data=model_uri_tipo,
    role=role,
    sagemaker_session=session
)

# Modelo de urgencia
model_urgencia = Model(
    image_uri=xgb_image,
    model_data=model_uri_urgencia,
    role=role,
    sagemaker_session=session
)

# Desplegar ambos modelos en endpoints distintos
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