"""
TAREA DE PROCESAMIENTO DE DATOS
Fecha realizada: 27-10-2026
Estado: En proceso

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

# %%
