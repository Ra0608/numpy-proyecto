import requests

def descargar_y_guardar_csv(url, nombre_archivo):
    try:
        # Realizar un GET request a la URL
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la respuesta es exitosa

        # Escribir la respuesta en un archivo CSV
        with open(nombre_archivo, 'w') as archivo_csv:
            archivo_csv.write(response.text)

        print(f"Datos descargados y guardados en '{nombre_archivo}'")

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar los datos: {e}")
    except Exception as e:
        print(f"Error al guardar los datos como CSV: {e}")

# Llamar a la función con la URL proporcionada y un nombre de archivo
url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
nombre_archivo = "datos_descargados.csv"
descargar_y_guardar_csv(url_datos, nombre_archivo)
