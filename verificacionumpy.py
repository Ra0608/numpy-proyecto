import pandas as pd
from datasets import load_dataset

# Cargar el dataset
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Convertir la estructura Dataset en un DataFrame de Pandas
df = pd.DataFrame(data)

# Verificar los tipos de datos en cada columna
tipos_de_datos = df.dtypes
print("Tipos de datos en cada columna:")
print(tipos_de_datos)

# Calcular la cantidad de hombres fumadores vs mujeres fumadoras
conteo_fumadores_por_genero = df.groupby(['is_male', 'is_smoker']).size().unstack()
conteo_fumadores_por_genero.columns = ['No Fumador', 'Fumador']

print("\nCantidad de hombres y mujeres fumadores:")
print(conteo_fumadores_por_genero)
