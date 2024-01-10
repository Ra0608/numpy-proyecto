# importa libreria numpy
import numpy as np
# importa datos de un dataset de paciente 
from datasets import load_dataset

# Conectar dataset 
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Obtener la lista de edades
edades = data['age']

# Convertir la lista de edades a un arreglo de NumPy
edades_np = np.array(edades)

# Calcular el promedio de edad
promedio_edad = np.mean(edades_np)

# imprimir el promedio de eadad en años 
print(f"El promedio de edad de las personas participantes en el estudio es: {promedio_edad} años.")

"""Al indexar por una característica, obtenemos una lista con los valores de todos los registros para esa colúmna.
Tu tarea para esta etapa del proyecto integrador es convertir la lista de edades a un arreglo de NumPy y calcular el promedio de edad de las personas participantes en el estudio."""