import pandas as pd
import numpy as np

def procesar_datos(dataframe):
    # Verificar valores faltantes
    if dataframe.isnull().values.any():
        print("Existen valores faltantes.")
        dataframe.dropna(inplace=True)
        print("Valores faltantes eliminados.")

    # Verificar filas repetidas
    if dataframe.duplicated().any():
        print("Existen filas repetidas.")
        dataframe.drop_duplicates(inplace=True)
        print("Filas repetidas eliminadas.")

    # Verificar y eliminar valores atípicos
    q1 = dataframe.quantile(0.25)
    q3 = dataframe.quantile(0.75)
    iqr = q3 - q1
    dataframe = dataframe[~((dataframe < (q1 - 1.5 * iqr)) | (dataframe > (q3 + 1.5 * iqr))).any(axis=1)]
    print("Valores atípicos eliminados.")

    # Crear columna de categoría por edades
    bins = [0, 12, 19, 39, 59, np.inf]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    dataframe['Categoria Edades'] = pd.cut(dataframe['Edad'], bins=bins, labels=labels, right=False)

    # Guardar el resultado como CSV
    dataframe.to_csv('datos_procesados.csv', index=False)
print("Resultados guardados como 'datos_procesados.csv'.")





