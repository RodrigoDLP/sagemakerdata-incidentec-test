import pandas as pd
import random
from datetime import datetime, timedelta
from locationdata import *
DATA_AMOUNT = 10000


def generate_data():
    data = []
    start = datetime(2025, 1, 1)
    for i in range(DATA_AMOUNT):
        urgencia = random.choices(urgencias, weights=urgencias_pesos, k=1)[0]
        ubicacion = random.choice(ubicaciones)
        if ubicacion in ubicaciones_sin_datos:
            if ubicacion == "aula":
                escogida = random.choice(list(aulas_datos.keys()))
                piso = aulas_datos[escogida][0]
                es_fase_2 = aulas_datos[escogida][1]
            elif ubicacion == "laboratorio":
                escogida = random.choice(list(laboratorios_datos.keys()))
                piso = laboratorios_datos[escogida][0]
                es_fase_2 = laboratorios_datos[escogida][1]
            elif ubicacion == "oficina":
                escogida = random.choice(list(oficinas_datos.keys()))
                piso = oficinas_datos[escogida][0]
                es_fase_2 = oficinas_datos[escogida][1]
            elif ubicacion == "sala de estudio":
                escogida = random.choice(list(salas_estudio_datos.keys()))
                piso = salas_estudio_datos[escogida][0]
                es_fase_2 = salas_estudio_datos[escogida][1]
            else:
                escogida = None
                piso = random.randint(1, 13) - 2
                es_fase_2 = False
        else:
            escogida = None
            piso = ubicaciones_datos[ubicacion][0]
            es_fase_2 = ubicaciones_datos[ubicacion][1]
        tipo = random.choices(tipos, weights=tipos_pesos, k=1)[0]
        fecha_hora = start + timedelta(minutes=random.randint(0, 60 * 24 * 300))  # fechas en un rango de 300 días
        data.append([urgencia, ubicacion, escogida, piso, es_fase_2, tipo, fecha_hora.strftime("%Y-%m-%d %H:%M:%S")])
    df = pd.DataFrame(data, columns=["urgencia", "ubicacion", "ubicacion_especifica", "piso", "es_fase_2", "tipo", "fecha_hora"])
    df.to_csv("incidents_model.csv", index=False)

def update_dataset(urgencia, ubicacion, tipo, fecha_hora):
    if ubicacion.lower() in ubicaciones_sin_datos:
        if ubicacion.lower() == "aula":
            escogida = random.choice(list(aulas_datos.keys()))
            piso = aulas_datos[escogida][0]
            es_fase_2 = aulas_datos[escogida][1]
        elif ubicacion.lower() == "laboratorio":
            escogida = random.choice(list(laboratorios_datos.keys()))
            piso = laboratorios_datos[escogida][0]
            es_fase_2 = laboratorios_datos[escogida][1]
        elif ubicacion.lower() == "oficina":
            escogida = random.choice(list(oficinas_datos.keys()))
            piso = oficinas_datos[escogida][0]
            es_fase_2 = oficinas_datos[escogida][1]
        elif ubicacion.lower() == "sala de estudio":
            escogida = random.choice(list(salas_estudio_datos.keys()))
            piso = salas_estudio_datos[escogida][0]
            es_fase_2 = salas_estudio_datos[escogida][1]
        else:
            escogida = None
            piso = None
            es_fase_2 = None
    else:
        escogida = None
        piso = ubicaciones_datos[ubicacion.lower()][0]
        es_fase_2 = ubicaciones_datos[ubicacion.lower()][1]
    nueva_fila = pd.DataFrame([{
        "urgencia": urgencia,
        "ubicacion": ubicacion.lower(),
        "ubicacion_especifica": escogida,
        "piso": piso,
        "es_fase_2": es_fase_2,
        "tipo": tipo,
        "fecha_hora": fecha_hora
    }])
    nueva_fila.to_csv("incidents_model.csv", mode="a", header=False, index=False)






generate_data()