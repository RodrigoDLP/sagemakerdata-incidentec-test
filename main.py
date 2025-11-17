from fastapi import FastAPI
from schemas import *
import boto3
import json

app = FastAPI()
runtime = boto3.client("sagemaker-runtime")

@app.post("/predict")
def predict(features: EndpointFeatures):
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

    response = runtime.invoke_endpoint(
        EndpointName=features.endpoint_name,
        ContentType="text/csv",
        Body=payload
    )

    result = response["Body"].read().decode("utf-8")
    return {"prediction": result}