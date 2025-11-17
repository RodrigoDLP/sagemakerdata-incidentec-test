import boto3
import pandas as pd
from sklearn.model_selection import train_test_split

def dataset_to_numbers():
    df = pd.read_csv("incidents_model.csv")
    df["urgencia"] = df["urgencia"].astype("category").cat.codes
    df["ubicacion"] = df["ubicacion"].astype("category").cat.codes
    df["ubicacion_especifica"] = df["ubicacion_especifica"].astype("category").cat.codes
    df["fecha_hora"] = pd.to_datetime(df["fecha_hora"])
    df["año"] = df["fecha_hora"].dt.year
    df["mes"] = df["fecha_hora"].dt.month
    df["día"] = df["fecha_hora"].dt.day
    df["hora"] = df["fecha_hora"].dt.hour
    df["dia_semana"] = df["fecha_hora"].dt.weekday
    df["es_fase_2"] = df["es_fase_2"].astype("int")
    df["tipo"] = df["tipo"].astype("category").cat.codes
    df = df.drop(columns=["fecha_hora"])
    df.to_csv("incidents_model_numbers.csv", index=False)
    print("Dataset pasado a números correctamente")

from sklearn.model_selection import train_test_split
import pandas as pd

def dataset_split(target_col="tipo"):
    df = pd.read_csv("incidents_model_numbers.csv")

    X = df.drop(columns=[target_col])
    y = df[target_col]

    df_final = pd.concat([y, X], axis=1)

    train_df, temp_df = train_test_split(df_final, test_size=0.30, random_state=42,
        shuffle=True, stratify=y)
    val_df, test_df = train_test_split(temp_df, test_size=0.50, random_state=42,
        shuffle=True, stratify=temp_df[target_col])

    train_df.to_csv(f"incidents_train_{target_col}.csv", index=False, header=False)
    val_df.to_csv(f"incidents_validation_{target_col}.csv", index=False, header=False)
    test_df.to_csv(f"incidents_test_{target_col}.csv", index=False, header=False)

    print(f"Datasets para predecir '{target_col}' generados correctamente")







dataset_to_numbers()
dataset_split("tipo")
dataset_split("urgencia")