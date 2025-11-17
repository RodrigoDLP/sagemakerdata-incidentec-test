from fastapi import FastAPI
from schemas import *
import boto3
import json

app = FastAPI()

# Cliente de SageMaker Runtime
runtime = boto3.client("sagemaker-runtime")

ENDPOINT_NAME = "mi-endpoint-incidentes"


@app.post("/predict")
def predict(features: IncidentFeatures):
    # Convertir a vector CSV (como espera XGBoost)
    payload = ",".join(map(str, [
        features.ubicacion,
        features.ubicacion_especifica,
        features.piso,
        features.es_fase_2,
        features.tipo,
        features.año,
        features.mes,
        features.día,
        features.hora,
        features.dia_semana
    ]))

    # Invocar el endpoint de SageMaker
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType="text/csv",
        Body=payload
    )

    # Leer la predicción
    result = response["Body"].read().decode("utf-8")

    return {"prediction": result}