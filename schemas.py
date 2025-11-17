
from pydantic import BaseModel

class EndpointFeatures(BaseModel):
    endpoint_name: str
    ubicacion: int
    ubicacion_especifica: int
    piso: int
    es_fase_2: int
    tipo: int
    ano: int
    mes: int
    dia: int
    hora: int
    dia_semana: int