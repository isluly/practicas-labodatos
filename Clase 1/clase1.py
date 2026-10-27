
"""
CLASE 01 - INTRODUCCIÓN A PYTHON I

MATERIA: Laboratorio de Datos
FECHA: 2° cuatrimestre 2026
ESTADO: En proceso

"""
#%% Ejercicio 1

"""

Definir una función leer_parque(nombre_archivo, parque) que abra el
archivo indicado y devuelva una lista de diccionarios con la información del
parque especificado. La lista debe tener un diccionario por cada árbol del parque
elegido. Dicho diccionario debe tener los datos correspondientes a un árbol
(recordar que cada fila del csv corresponde a un árbol).
Probar la función en el parque ‘GENERAL PAZ’ y debería dar una lista con 690
árboles.

"""

def leer_parque(nombre_archivo, parque):
        with open (nombre_archivo,'rt') as f: 
                filas = csv.reader(f)
                
