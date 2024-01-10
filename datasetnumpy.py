import numpy as np
import pandas as pd
from datasets import load_dataset

# Cargar el dataset
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Convertir la estructura Dataset en un DataFrame con Pandas
df = pd.DataFrame(data)

# Separar el dataframe en dos según el valor de 'is_dead'
df_perecieron = df[df['is_dead'] == 1]
df_sobrevivieron = df[df['is_dead'] == 0]

# Calcular el promedio de edades para cada dataset
promedio_edad_perecieron = np.mean(df_perecieron['age'])
promedio_edad_sobrevivieron = np.mean(df_sobrevivieron['age'])

print(f"Promedio de edad de personas que perecieron: {promedio_edad_perecieron} años.")
print(f"Promedio de edad de personas que sobrevivieron: {promedio_edad_sobrevivieron} años.")