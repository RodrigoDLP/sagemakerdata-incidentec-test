import pandas as pd
from sklearn.datasets import dump_svmlight_file

df_train_tipo = pd.read_csv("incidents_train_tipo.csv")
df_train_urgencia = pd.read_csv("incidents_train_urgencia.csv")
df_validation_tipo = pd.read_csv("incidents_validation_tipo.csv")
df_validation_urgencia = pd.read_csv("incidents_validation_urgencia.csv")
df_test_tipo = pd.read_csv("incidents_test_tipo.csv")
df_test_urgencia = pd.read_csv("incidents_test_urgencia.csv")

y_train_tipo = df_train_tipo.iloc[:, 0]
x_train_tipo = df_train_tipo.iloc[:, 1:]
y_train_urgencia = df_train_urgencia.iloc[:, 0]
x_train_urgencia = df_train_urgencia.iloc[:, 1:]
y_validation_tipo = df_validation_tipo.iloc[:, 0]
x_validation_tipo = df_validation_tipo.iloc[:, 1:]
y_validation_urgencia = df_validation_urgencia.iloc[:, 0]
x_validation_urgencia = df_validation_urgencia.iloc[:, 1:]
y_test_tipo = df_test_tipo.iloc[:, 0]
x_test_tipo = df_test_tipo.iloc[:, 1:]
y_test_urgencia = df_test_urgencia.iloc[:, 0]
x_test_urgencia = df_test_urgencia.iloc[:, 1:]

dump_svmlight_file(x_train_tipo, y_train_tipo, "incidents_train_tipo.libsvm")
dump_svmlight_file(x_train_urgencia, y_train_urgencia, "incidents_train_urgencia.libsvm")
dump_svmlight_file(x_validation_tipo, y_validation_tipo, "incidents_validation_tipo.libsvm")
dump_svmlight_file(x_validation_urgencia, y_validation_urgencia, "incidents_validation_urgencia.libsvm")
dump_svmlight_file(x_test_tipo, y_test_tipo, "incidents_test_tipo.libsvm")
dump_svmlight_file(x_test_urgencia, y_test_urgencia, "incidents_test_urgencia.libsvm")
print("Data de entrenamiento, validación y test pasada correctamente a formato LIBSVM")