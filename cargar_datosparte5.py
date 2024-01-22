# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np

# Definir una función llamada procesar_datos que toma un DataFrame como entrada
def procesar_datos(dataframe):
    # Verificar si hay valores faltantes en el DataFrame
    if dataframe.isnull().values.any():
        print("Existen valores faltantes en los datos.")
        # Eliminar las filas con valores faltantes
        dataframe.dropna(inplace=True)
        print("Valores faltantes eliminados.")

    # Verificar si hay filas duplicadas en el DataFrame
    if dataframe.duplicated().any():
        print("Existen filas duplicadas en los datos.")
        # Eliminar las filas duplicadas
        dataframe.drop_duplicates(inplace=True)
        print("Filas duplicadas eliminadas.")

    # Verificar y eliminar valores atípicos usando el rango intercuartil (IQR)
    q1 = dataframe.quantile(0.25)
    q3 = dataframe.quantile(0.75)
    iqr = q3 - q1
    # Mantener solo las filas que no contienen valores atípicos
    dataframe = dataframe[~((dataframe < (q1 - 1.5 * iqr)) | (dataframe > (q3 + 1.5 * iqr))).any(axis=1)]
    print("Valores atípicos eliminados.")

    # Crear una nueva columna llamada 'Categoria Edades' basada en las edades de las personas
    bins = [0, 12, 19, 39, 59, np.inf]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    dataframe['Categoria Edades'] = pd.cut(dataframe['Edad'], bins=bins, labels=labels, right=False)

    # Guardar el DataFrame procesado como un nuevo archivo CSV llamado 'datos_procesados.csv'
    dataframe.to_csv('datos_procesados.csv', index=False)
print("Resultados guardados como 'datos_procesados.csv'.")






