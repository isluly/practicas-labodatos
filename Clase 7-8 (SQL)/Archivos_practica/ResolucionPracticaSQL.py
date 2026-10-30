"""
PRÁCTICA SQL - CLASES 7-8

La presente práctica busca que podamos realizar consultas relativamente simples en SQL

Fecha: 29-10-2026

Estado: TERMINADA

"""
#%% IMPORTS

import duckdb as db
import pandas as pd
from pathlib import Path

#%% ARCHIVOS

carpeta = Path(__file__).parent.resolve().as_posix() + "/"

casos = pd.read_csv(carpeta + "casos.csv")
departamentos = pd.read_csv(carpeta + "departamento.csv")
grupoetario = pd.read_csv(carpeta + "grupoetario.csv")
provincias = pd.read_csv(carpeta + "provincia.csv")
tipoevento = pd.read_csv(carpeta + "tipoevento.csv")


#%% Ejemplo de consulta

#print (empleado)

#consultaSQL = """
   
#    SELECT DISTINCT DNI, Salario
#    FROM empleado;
#    """


#dataframeResultado = db.sql(conultaSQL).df()
#print(dataframeResultado)

#%% EJERCICIO 1 - Consultas sobre una tabla

consulta01 = """
    SELECT descripcion
    FROM departamentos;
    """

df01= db.sql(consulta01).df()
print (df01)

consulta02 = """
    SELECT DISTINCT descripcion
    FROM departamentos;
    """

df02= db.sql(consulta02).df()
print (df02)

consulta03 = """
    SELECT descripcion, id
    FROM departamentos;
    """

df03= db.sql(consulta03).df()
print (df03)

consulta04 = """
    SELECT *
    FROM departamentos;
    """
df04 = db.sql(consulta04).df()
print(df04)

consulta05 = """
    SELECT id AS codigo_depto, descripcion AS nombre_depto
    FROM departamentos;
    """
df05 = db.sql(consulta05).df()
print(df05)    

consulta06 = """
    SELECT *
    FROM departamentos
    WHERE id_provincia = 54;
    """
df06 = db.sql(consulta06).df()
print(df06)

consulta07 = """
    SELECT *
    FROM departamentos
    WHERE id_provincia = 22 OR id_provincia = 78 OR id_provincia = 86;
    """
df07 = db.sql(consulta07).df()
print(df07)

consulta08 = """
    SELECT *
    FROM departamentos
    WHERE id_provincia >= 50 AND id_provincia <= 59;
    """
df08 =db.sql(consulta08).df()
print(df08)

#%% EJERCICIO 02 -Consultas multitabla (inner join)

consulta09 = """
    SELECT d.id AS codigo_depto, 
    d.descripcion AS nombre_depto, 
    p.descripcion AS nombre_provincia
    FROM departamentos AS d
    INNER JOIN provincias as p
    ON d.id_provincia = p.id;
    """
df09 = db.sql(consulta09).df()
print(df09)

consulta10 = """
    SELECT c.*
    FROM casos AS c
    INNER JOIN departamentos AS d 
    ON c.id_depto = d.id
    INNER JOIN provincias AS p
    ON d.id_provincia = p.id
    WHERE p.descripcion = 'Chaco';
    """
df10 = db.sql(consulta10).df()
print(df10)    

consulta11 = """
    SELECT c.*
    FROM casos AS c
    INNER JOIN departamentos AS d 
    ON c.id_depto = d.id
    INNER JOIN provincias AS p
    ON d.id_provincia = p.id
    WHERE p.descripcion = 'Buenos Aires' AND c.cantidad > 10;
    """
df11 = db.sql(consulta11).df()
print(df11) 

# %% EJERCICIO 03 - Consultas multitabla (outer join)

consulta12 = """
    SELECT d.descripcion AS nombre_depto
    FROM departamentos AS d
    FULL JOIN casos AS c
    ON d.id = c.id_depto
    WHERE c.cantidad IS NULL
    """

df12 =db.sql(consulta12).df()
print(df12)

consulta13 = """
    SELECT t.descripcion AS no_hay_casos
    FROM tipoevento AS t
    LEFT JOIN casos AS C
    ON t.id = c.id_tipoevento
    WHERE c.cantidad IS NULL;
    """
df13 =db.sql(consulta13).df()
print(df13)
    
#%% Ejercicio 04 -Consultas Resumen
print ('=' *34)
print ('CONSULTA 14')
print ('=' *34)

consulta14 = """
    SELECT SUM(c.cantidad) AS cantidad_casos
    FROM casos AS c
    """
df14 = db.sql(consulta14).df()
print(df14)

print ('=' *34)
print ('CONSULTA 15')
print ('=' *34)

consulta15= """
    SELECT t.descripcion AS tipoDeCaso,
           c.anio AS año,
           SUM (c.cantidad) AS cant_casos

           
    FROM tipoevento as t
    INNER JOIN casos as c
    ON t.id = c.id_tipoevento
    GROUP BY t.descripcion, c.anio
    ORDER BY cant_casos ASC, c.anio ASC;
    """
df15 = db.sql(consulta15).df()
print(df15)

print ('=' *34)
print ('CONSULTA 16')
print ('=' *34)

consulta16= """
    SELECT t.descripcion AS tipoDeCaso,
           c.anio AS año,
           SUM(c.cantidad) AS cant

    FROM tipoevento as t
    INNER JOIN casos as c
    ON t.id = c.id_tipoevento AND c.anio = 2019
    GROUP BY t.descripcion, c.anio
    """
df16 = db.sql(consulta16).df()
print(df16)

print ('=' *34)
print ('CONSULTA 17')
print ('=' *34)

consulta17 = """
    SELECT p.id, count(*) AS cantidad_deptos
    FROM provincias AS p
    INNER JOIN departamentos as d
    ON p.id = d.id_provincia
    GROUP BY p.id
    ORDER BY p.id ASC
    """
df17 = db.sql(consulta17).df()
print(df17)

print ('=' *34)
print ('CONSULTA 18')
print ('=' *34)

consulta18 = """
    SELECT d.descripcion, SUM(c.cantidad) AS cantidad_casos
    FROM departamentos AS d
    INNER JOIN casos as c
    ON d.id = c.id_depto
    WHERE c.anio = 2019
    GROUP BY d.id, d.descripcion
    ORDER BY cantidad_casos ASC;
    """
df18 = db.sql(consulta18).df()
print(df18)

print ('=' *34)
print ('CONSULTA 19')
print ('=' *34)

consulta19 = """
    SELECT d.descripcion, SUM(c.cantidad) AS cantidad_casos
    FROM departamentos AS d
    INNER JOIN casos AS c
    ON d.id = c.id_depto
    WHERE c.anio = 2020
    GROUP BY d.id, d.descripcion
    ORDER BY cantidad_casos DESC;
    """
df19 = db.sql(consulta19).df()
print(df19)
    
print ('=' *34)
print ('CONSULTA 20')
print ('=' *34)

consulta20= """
    SELECT p.descripcion AS provincia , c.anio AS año, AVG(c.cantidad) AS promedio
    FROM provincias AS p
    INNER JOIN departamentos AS d 
    ON p.id = d.id_provincia
    INNER JOIN casos AS c
    ON d.id = c.id_depto
    GROUP BY c.anio, p.descripcion
    ORDER BY p.descripcion ASC;
    """
df20 = db.sql(consulta20).df()
print(df20)

print ('=' *34)
print ('CONSULTA 21')
print ('=' *34)

consulta21= """
    SELECT p.descripcion AS provincia,
           c.anio AS año,
           d.descripcion AS depto,
           SUM(c.cantidad) AS cantidad_casos
    FROM provincias as p
    INNER JOIN departamentos as d
    ON p.id = d.id_provincia
    INNER JOIN casos AS c
    ON d.id = c.id_depto
    GROUP BY p.descripcion, c.anio, d.descripcion
    ORDER BY cantidad_casos DESC;
    """
df21= db.sql(consulta21).df()
print(df21)

print ('=' *34)
print ('CONSULTA 22')
print ('=' *34)

consulta22="""
    SELECT p.descripcion AS provincia,
    MAX(c.cantidad) AS max,
    MIN(c.cantidad) AS min,
    AVG(c.cantidad) AS promedio
    FROM provincias as p
    INNER JOIN departamentos AS d
    ON p.id = d.id_provincia
    INNER JOIN casos AS c
    ON d.id = c.id_depto
    WHERE p.id = 6 AND c.anio = 2019
    GROUP BY p.descripcion
    """
df22 = db.sql(consulta22).df()
print(df22)

print ('=' *34)
print ('CONSULTA 23')
print ('=' *34)


consulta23="""
    SELECT p.descripcion AS provincia,
    MAX(c.cantidad) AS max,
    MIN(c.cantidad) AS min,
    AVG(c.cantidad) AS promedio
    FROM provincias as p
    INNER JOIN departamentos AS d
    ON p.id = d.id_provincia
    INNER JOIN casos AS c
    ON d.id = c.id_depto
    WHERE p.id = 6 AND c.anio = 2019 AND c.cantidad > 1000
    GROUP BY p.descripcion
    """
df23 = db.sql(consulta23).df()
print(df23)

print ('=' *34)
print ('CONSULTA 24')
print ('=' *34)

consulta24 = """
    SELECT p.descripcion AS provincia,
    d.descripcion AS depto,
    AVG(c.cantidad) AS promedio
    FROM provincias as p
    INNER JOIN departamentos as d
    ON p.id = d.id_provincia
    INNER JOIN casos as c
    ON d.id = c.id_depto
    GROUP BY d.descripcion, p.descripcion
    HAVING COUNT (DISTINCT c.anio) = 2
    ORDER BY provincia ASC, depto ASC;
    """
df24 = db.sql(consulta24).df()
print(df24)

print ('=' *34)
print ('CONSULTA 25')
print ('=' *34)

consulta25 = """
    SELECT t.descripcion AS 'descripcion de tipo de evento',
    d.id AS id_depto,
    d.descripcion AS 'nombre de departamento',
    p.id AS id_provincia,
    p.descripcion AS 'nombre de provincia',
    SUM(CASE WHEN c.anio = 2019 THEN c.cantidad ELSE 0 END) AS total_2019,
    SUM(CASE WHEN c.anio = 2020 THEN c.cantidad ELSE 0 END) AS total_2020
    FROM provincias AS p
    INNER JOIN departamentos as d
    ON p.id = d.id_provincia
    INNER JOIN casos AS c
    ON d.id = c.id_depto
    INNER JOIN tipoevento AS t
    ON c.id_tipoevento = t.id
    GROUP BY t.descripcion, d.id, d.descripcion, p.id, p.descripcion
    ORDER BY p.descripcion ASC, d.descripcion ASC;
    """
df25= db.sql(consulta25).df()
print (df25)

#%% EJERCICIO 5 -Subconsultas (ALL, ANY)

print ('=' *34)
print ('CONSULTA 26')
print ('=' *34)

consulta26 = """
    SELECT d.descripcion AS departamento,
    c.cantidad AS cantidad
    FROM departamentos as d
    INNER JOIN casos as c
    ON d.id = c.id_depto
    WHERE c.cantidad >= ALL (
        SELECT c1.cantidad
        FROM casos AS c1
        );
    """

df26= db.sql(consulta26).df()
print(df26)

print ('=' *34)
print ('CONSULTA 27')
print ('=' *34)

consulta27= """
    SELECT t.descripcion AS tipo_evento 
    FROM tipoevento AS t
    INNER JOIN casos as c 
    ON t.id = c.id_tipoevento
    WHERE t.descripcion = ANY (
        SELECT t1.descripcion
        FROM tipoevento as t1)
    GROUP BY tipo_evento;
    """
df27 = db.sql(consulta27).df()
print(df27)

#%% EJERCICIO 6 - Subconsultas (IN, NOT IN)

print ('=' *34)
print ('CONSULTA 28')
print ('=' *34)

consulta28 = """
    SELECT t.descripcion AS tipo_evento
    FROM tipoevento AS t
    WHERE t.id IN (
        SELECT c.id_tipoevento
        FROM casos AS c)
    GROUP BY tipo_evento
    """

df28= db.sql(consulta28).df()
print(df28)


print ('=' *34)
print ('CONSULTA 29')
print ('=' *34)

consulta29= """
    SELECT t.descripcion AS tipo_evento
    FROM tipoevento AS t
    WHERE t.id NOT IN (
        SELECT c.id_tipoevento
        FROM casos AS c)
    GROUP BY tipo_evento
    """
df29 = db.sql(consulta29).df()
print(df29)    

#%% EJERCICIO 7 - Subconsultas (EXISTS, NOT EXISTS)

print ('=' *34)
print ('CONSULTA 30')
print ('=' *34)

consulta30= """
    SELECT t.descripcion AS tipo_evento
    FROM tipoevento AS t
    WHERE EXISTS(
        SELECT 1
        FROM casos AS c
        WHERE c.id_tipoevento = t.id)
    """
df30 = db.sql(consulta30).df()
print(df30)

print ('=' *34)
print ('CONSULTA 31')
print ('=' *34)

consulta31= """
    SELECT t.descripcion AS tipo_evento
    FROM tipoevento AS t
    WHERE NOT EXISTS(
        SELECT 1
        FROM casos AS c
        WHERE c.id_tipoevento = t.id)
    """
df31 = db.sql(consulta31).df()
print(df31)

#%% EJERCICIO 8 - Subconsultas correlacionadas

print ('=' *34)
print ('CONSULTA 32')
print ('=' *34)

consulta32 = """
    SELECT p.descripcion AS provincia, 
    c.anio AS año,
    SUM(c.cantidad) AS cant
    FROM provincias as p 
    INNER JOIN departamentos as d
    ON p.id = d.id_provincia
    INNER JOIN casos as c
    ON d.id = c.id_depto
    GROUP BY p.id, p.descripcion, c.anio
    HAVING SUM(c.cantidad) > (
        SELECT AVG(c1.cantidad)
        FROM casos AS c1
        WHERE c1.anio =c.anio)
    ORDER BY provincia, año, cant;
    """
df32=  db.sql(consulta32).df()
print(df32)

print ('=' *34)
print ('CONSULTA 33')
print ('=' *34)

consulta33 = """
    SELECT p.descripcion AS provincia,
           c.anio AS año,
           SUM(c.cantidad) AS cant
    FROM provincias AS p
    INNER JOIN departamentos AS d
        ON p.id = d.id_provincia
    INNER JOIN casos AS c
        ON d.id = c.id_depto
    GROUP BY p.id, p.descripcion, c.anio
    HAVING SUM(c.cantidad) > (
        SELECT SUM(c1.cantidad)
        FROM casos AS c1
        WHERE c1.anio = c.anio
          AND EXISTS (
              SELECT 1
              FROM departamentos AS d1
              WHERE c1.id_depto = d1.id
                AND d1.id_provincia = 18
          )
    );
    """

df33=  db.sql(consulta33).df()
print(df33)

#%% EJERCICIO 9 -Más consultas sobre una tabla

print ('=' *34)
print ('CONSULTA 34')
print ('=' *34)

consulta34 = """
    SELECT DISTINCT d.id AS código,
    d.descripcion AS nombre_depto
    FROM departamentos AS d
    ORDER BY nombre_depto DESC, código ASC;
    """
df34 =db.sql(consulta34).df()
print(df34)

print ('=' *34)
print ('CONSULTA 35')
print ('=' *34)

consulta35 = """
    
    SELECT p.id AS id,
    p.descripcion AS nombre
    FROM provincias AS p
    GROUP BY id, nombre
    HAVING nombre LIKE 'M%'

"""
df35=db.sql(consulta35).df()
print(df35)

print ('=' *34)
print ('CONSULTA 36')
print ('=' *34)

consulta36 = """
    SELECT p.id AS id,
           p.descripcion AS nombre
    FROM provincias AS p
    WHERE (p.descripcion LIKE '%s%' OR p.descripcion LIKE '%S%')
      AND (p.descripcion LIKE '____a%' OR p.descripcion LIKE '____A%')
    """
df36 = db.sql(consulta36).df()
print(df36)

print ('=' *34)
print ('CONSULTA 37')
print ('=' *34)

consulta37="""
    SELECT p.id AS id,
    p.descripcion AS nombre
    FROM provincias AS p
    WHERE (nombre LIKE '%a')
    """
df37=db.sql(consulta37).df()
print(df37)

print ('=' *34)
print ('CONSULTA 38')
print ('=' *34)

consulta38 = """
    SELECT p.id AS id, 
    p.descripcion AS nombre
    FROM provincias AS p
    WHERE (nombre LIKE '_____')
    """
df38=db.sql(consulta38).df()
print(df38)

print ('=' *34)
print ('CONSULTA 39')
print ('=' *34)

consulta39 = """
    SELECT p.id AS id, 
    p.descripcion AS nombre
    FROM provincias AS p
    WHERE (nombre LIKE '%do%') AND (p.id < 30 )
    """
df39=db.sql(consulta39).df()
print(df39)

print ('=' *34)
print ('CONSULTA 40')
print ('=' *34)

consulta40 = """
    SELECT d.id AS codigo_depto,
    d.descripcion AS nombre_depto
    FROM departamentos AS d
    WHERE (d.descripcion LIKE '%San%')
    GROUP BY d.id, d.descripcion
    ORDER BY nombre_depto DESC
    """
df40=db.sql(consulta40).df()
print(df40)


print ('=' *34)
print ('CONSULTA 41')
print ('=' *34)

consulta41 = """
    SELECT p.descripcion AS 'nombre de provincia',
    d.descripcion AS 'nombre de depatartmento',
    c.anio AS año,
    c.semana_epidemiologica AS 'semana epidemiologica',
    c.id_grupoetario AS 'grupo etario',
    c.cantidad
    FROM provincias AS p
    INNER JOIN departamentos AS d
    ON p.id = d.id_provincia
    INNER JOIN casos AS c
    ON d.id = c.id_depto
    WHERE (p.descripcion LIKE '%a' AND c.cantidad > 10)
    GROUP BY p.descripcion, d.descripcion, c.anio, c.semana_epidemiologica, 
    c.id_grupoetario, c.cantidad
    ORDER BY cantidad DESC, p.descripcion ASC, d.descripcion ASC, c.anio ASC,
    c.id_grupoetario ASC
    """
df41= db.sql(consulta41).df()
print(df41)

print ('=' *34)
print ('CONSULTA 42')
print ('=' *34)

consulta42 = """
    SELECT p.descripcion AS provincia,
           d.descripcion AS departamento,
           c.anio AS año,
           c.semana_epidemiologica,
           g.descripcion AS grupo_etario,
           c.cantidad
    FROM casos AS c
    INNER JOIN departamentos AS d ON c.id_depto = d.id
    INNER JOIN provincias AS p ON d.id_provincia = p.id
    INNER JOIN grupoetario AS g ON c.id_grupoetario = g.id
    WHERE LOWER(p.descripcion) LIKE '%a'
      AND c.cantidad > 10
      AND c.cantidad = (
          SELECT MAX(c1.cantidad)
          FROM casos AS c1
          INNER JOIN departamentos AS d1 ON c1.id_depto = d1.id
          INNER JOIN provincias AS p1 ON d1.id_provincia = p1.id
          WHERE LOWER(p1.descripcion) LIKE '%a'
            AND c1.cantidad > 10
      )
    ORDER BY c.cantidad DESC,
             p.descripcion ASC,
             d.descripcion ASC,
             c.anio ASC,
             g.descripcion ASC
    """

df43 = db.sql(consulta42).df()
print(df43)
df42= db.sql(consulta42).df()
print(df42)

#%% EJERCICIO 10 -Reemplazos

print ('=' *34)
print ('CONSULTA 43')
print ('=' *34)

consulta43 = """
    SELECT id,
           REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(
           REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(
               descripcion,
               'á', 'a'), 'é', 'e'), 'í', 'i'), 'ó', 'o'), 'ú', 'u'),
               'Á', 'A'), 'É', 'E'), 'Í', 'I'), 'Ó', 'O'), 'Ú', 'U')
           AS descripcion
    FROM departamentos
    ORDER BY descripcion ASC
    """

df43 = db.sql(consulta43).df()
print(df43)

print ('=' *34)
print ('CONSULTA 44')
print ('=' *34)

consulta44 = """
    SELECT REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(
               UPPER(descripcion),
               'Á', 'A'), 'É', 'E'), 'Í', 'I'), 'Ó', 'O'), 'Ú', 'U')
           AS provincia
    FROM provincias
    ORDER BY provincia ASC
    """

df44 = db.sql(consulta44).df()
print(df44)