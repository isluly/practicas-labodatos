"""
PRACTICA 00 - INTRODUCCIÓN A PYTHON

MATERIA: Laboratorio de Datos
FECHA: 2° cuatrimestre 2026
ESTADO: Resuelta

"""

#%% imports

import pandas as pd

#%% Ejercicio 1

"""
Una mañana ponés un billete en la vereda al lado del obelisco porteño. A partir
de ahí, cada día vas y duplicás la cantidad de billetes, apilándolos prolijamente.
¿Cuánto tiempo pasa antes de que la pila de billetes sea más alta que el
obelisco?
Datos: espesor del billete: 0.11 mm, altura obelisco: 67.5 m.
"""
def billetesAObelisco ():
    bill = 0.11 #milimetros
    obelisco = 67500 #67.5 metros a milimetros
    pila = bill #al iniciar no hay billetes
    dias = 1

    while pila < obelisco:
        dias += 1
        pila += pila 

    return dias


# %% Ejercicio 2

"""
Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o
'pu' según corresponda luego de cada vocal.
Ejemplo:
cadena = 'Casa'
cadena_geringosa = ''
for c in cadena:
COMPLETAR
print(cadena_geringosa)
# Geperipingoposopo
Luego hacelo con un while en vez del for.

"""

def geringoso (palabra):
    cadena = palabra.lower()
    cadena_geringosa = ''
    vocales = ['a','e','i','o','u']
    for c in cadena:
        if c in vocales:
            cadena_geringosa += c+'p'+c
        else:
            cadena_geringosa += c
    return cadena_geringosa

def geringoso_while(palabra):
    cadena = palabra.lower()
    cadena_geringosa = ''
    vocales = ['a','e','i','o','u']
    letra = 0

    while letra < len(cadena):
        if cadena[letra] in vocales:
            cadena_geringosa += cadena[letra]+'p'+ cadena[letra]
        else:
            cadena_geringosa += cadena[letra]
        
        letra += 1
    return cadena_geringosa
        
# %% Ejercicio 3

"""
Definir una función pertenece(lista, elem) que tome una lista y un
elemento, y devuelva True si la lista tiene al elemento dado y False en caso
contrario.
"""

def pertenece (lista,elem):
    return elem in lista

# %% Ejercicio 4

"""
Definir una función mas_larga(lista1, lista2) que tome dos listas y
devuelva la más larga.
"""

def mas_larga(lista1,lista2):
    assert len(lista1) != len(lista2), 'Las listas son igual de largas'
    if len(lista1) < len(lista2):
        return lista2
    else:
        return lista1

# %% Ejercicio 5
"""
Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que
toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa
rebotes.py que imprima una tabla mostrando las alturas que alcanza en cada uno
de sus primeros diez rebotes.

"""
def caida_pelota():
    altura = 100
    rebotes = 10
    print("Rebote\tAltura")
    for i in range(1, rebotes + 1):
        altura *= 3/5
        print(f"{i}\t{altura:.2f}")


# %% Ejercicio 6

"""
Definir la función mezclar(cadena1, cadena2) que tome dos strings y
devuelva el resultado de intercalar elemento a elemento. Por ejemplo: si
intercalamos Pepe con Jose daría PJeopsee. En el caso de Pepe con Josefa daría
PJeopseefa 

"""
def mezclar(cadena1,cadena2):
    long1 = len(cadena1)
    long2 = len(cadena2)
    cadena_final = ''


    if long1<long2:
        i = 0
        while i < long1:
            cadena_final+= cadena1[i] + cadena2[i]
            i += 1
        cadena_final += cadena2[i:]

    else: 
        i = 0
        while i < long2:
            cadena_final += cadena1[i] + cadena2[i]
            i+=1
        cadena_final += cadena1[i:]
    return cadena_final
# %%  Ejercicio 7

"""
David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija
nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de
$2684,11.
a. Escribir un programa que calcula el monto total que pagará David a lo
largo de los años. Deberías obtener que en total paga $966279.6.
b. Supongamos que David adelanta pagos extra de $1000/mes durante los
primeros 12 meses de la hipoteca. Modificá el programa para incorporar
estos pagos extra y que imprima el monto total pagado junto con la
cantidad de meses requeridos. Deberías obtener que el pago total es de
$929965.62 en 342 meses.
c. ¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años,
comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?
Modificá tu programa de forma que la información sobre pagos extras sea
incorporada de manera versátil. Sugerimos utilizar los parámetros:
pago_extra_monto, pago_extra_mes_comienzo, pago_extra_mes_fin.

"""
def pagoDavid_con_adelanto(
    pago_extra_monto=0,
    pago_extra_mes_comienzo=0,
    pago_extra_mes_fin=0
):
    tasa_mensual = 0.05 / 12
    falta_devolver = 500000
    cuota = 2684.11
    pago_total = 0 
    mes = 1

    while falta_devolver > 0:
        falta_devolver *= 1 + tasa_mensual
        pago = cuota

        if pago_extra_mes_comienzo <= mes <= pago_extra_mes_fin:
            pago += pago_extra_monto

        falta_devolver -= pago
        pago_total += pago
        mes += 1

    return pago_total, mes - 1


# %% Ejercicio 8

"""
Construí una función traductor_geringoso(lista) que, a partir de una lista de
palabras, devuelva un diccionario geringoso. Las claves del diccionario deben ser
las palabras de la lista y los valores deben ser sus traducciones al geringoso.
Por ejemplo, al tomar la lista ['banana', 'manzana', 'mandarina'] debe
devolver {'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa',
'mandarina': 'mapandaparipinapa'}.
"""

def traductor_geringoso(lista):
    dict = {}
    for palabra in lista:
        dict [palabra] = geringoso(palabra)
    return dict
    
# %% Ejercicio 9

"""
Escribí un programa que imprima de forma prolija las tablas de multiplicar del 1 al
9 usando f-strings. Si podés, evitá usar la multiplicación, usando sólo sumas
alcanza.

"""
print(f"{'':>4}", end="")
for columna in range(1, 10):
    print(f"{columna:>4}", end="")
print()

print("-" * 40)

for fila in range(1, 10):
    print(f"{fila:>3}|", end="")
    resultado = 0

    for columna in range(1, 10):
        resultado += fila
        print(f"{resultado:>4}", end="")

    print()

# %%
