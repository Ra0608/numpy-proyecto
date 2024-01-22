import requests
import pandas as pd
import numpy as np

def procesar_y_guardar_datos_proyecto(url):
    try:
        # Realizar un GET request a la URL
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la respuesta es exitosa

        # Escribir la respuesta en un archivo CSV
        with open('datos_proyecto.csv', 'w') as archivo_csv:
            archivo_csv.write(response.text)

        print("Datos descargados y guardados en 'datos_descargados.csv'")

        # Cargar el archivo CSV en un DataFrame
        df = pd.read_csv('datos_proyecto.csv')

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar los datos: {e}")
    except Exception as e:
        print(f"Error al procesar el DataFrame: {e}")

# Llamar a la función con la URL proporcionada
url_datos_proyecto = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
procesar_y_guardar_datos_proyecto(url_datos_proyecto)

