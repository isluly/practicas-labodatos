"""
TAREA DE PROCESAMIENTO DE DATOS
Fecha realizada: 27-10-2026
Estado: Terminada

"""
#%% Imports
import pandas as pd

#%% Actividad 1

empleado_01 = [[20222333,45,2,20000],[33456234,40,0,25000],[45432345,41,1,10000]]

def superanSalarioActividad01 (empleado_01, umbral):
    matriz = []
    for fila in empleado_01:
        if fila [3]>umbral:
            matriz.append(fila)
    return matriz

# %% Actividad 2

agregados = [[43967304,37,0,12000],[42238276,36,0,18000]]
empleado_02 = empleado_01 + agregados

# %% Actividad 3

empleado_03 = [[20222333,20000, 45, 2],
 [33456234, 25000, 40, 0],
 [45432345, 10000, 41, 1],
 [43967304, 12000, 37, 0],
 [42238276, 18000, 36, 0]]

def superanSalarioActividad03 (empleado_03, umbral):
    matriz = []
    for fila in empleado_03:
        if fila [1]>umbral:
            matriz.append(fila)
    return matriz

# %% Actividad 4

empleado_04 = [
    [20222333, 33456234, 45432345, 43967304, 42236276],  # DNI
    [20000, 25000, 10000, 12000, 18000],               # Salario
    [45, 40, 41, 37, 36],                            # Edad
    [2, 0, 1, 0, 0]                                 # Cantidad de hijos
]


def superanSalarioActividad04(empleado_04, umbral):
    resultado = []

    for i in range(len(empleado_04[0])):
        if empleado_04[1][i] > umbral:
            fila = [
                empleado_04[0][i],  # DNI
                empleado_04[2][i],  # Edad
                empleado_04[3][i],  # Cantidad de hijos
                empleado_04[1][i]   # Salario
            ]
            resultado.append(fila)

    return resultado

# %% Actividad 5

"""
01. ¿Cómo afectó a la proframación de la función
cuando cambiaron levemente la matriz de empleado?

Basicamente las soluciones estaban implementadas para
un tipo de estructura particular. Una simple modificación
en el orden de los elementos requería tunear la función.

El único caso que no presentó problemas fue el de empleado_02,
ya que agregar filas manteniendo el mismo orden era compatible con
la indexación utilizada originalmente. 

La modificación de la estructura de empleado_03 fue sencilla de
implementar. 

02. ¿Y cuando a empleado le cambiaron la forma de representar
las matrices (de lista de filas a lista de columnas)? 

Para realizar la actividad 4 fue necesario repensar
la función y como acceder a cada elemento. Fue el caso
más dificil. Y creo que no es la mejor forma de representar
estos datos porque uno tiene que reconstruir la información
de la 'persona' a partir de un elemento de cada columna (en este caso, de cada
fila de la matriz). Esto hace que el código sea más difícil de leer 
y mantener, y aumenta la probabilidad de errores al acceder a los datos.

03. ¿Cuál es la ventaja, desde el punto de vista del usuario de la función,
disponer de ella y no escribir directamente el código de la consulta
dentro de su programa?

Claramente es mucho más sencillo no tener que implementar la función
cada vez que se necesite realizar la misma consulta. Ya que puede resultar
engorroso. 

"""
