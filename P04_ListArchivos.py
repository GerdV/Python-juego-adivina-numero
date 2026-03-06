# PANDAS
# Pandas es un paquete de software de código abierto para la manipulación y análisis de datos 
# en Python. Proporciona estructuras de datos y funciones para trabajar con datos tabulares, 
# como DataFrames, que son similares a las hojas de cálculo o tablas de bases de datos. 
# Pandas es ampliamente utilizado en la ciencia de datos, análisis de datos y aprendizaje 
# automático debido a su facilidad de uso y eficiencia.    
# Para usar Pandas, primero debes instalarlo. Puedes hacerlo usando pip:
# pip install pandas

# Dataframe es una estructura de datos bidimensional que se asemeja a una tabla. Es una de las 
# estructuras de datos más utilizadas en Pandas y es muy útil para almacenar y manipular datos 
# tabulares. Un DataFrame puede contener diferentes tipos de datos (números, cadenas, fechas, 
# etc.) y tiene etiquetas para las filas y columnas.  

import pandas as pd
import os

data = {
    'Piezas:' : ["Tablero", "Silla", "Mesa", "Estante", "Puerta"],
    'Cantidad:' : [10, 20, 5, 15, 8],
    'Precio:' : [100, 50, 200, 150, 300]
}

df = pd.DataFrame(data) # Creamos un DataFrame a partir del diccionario de datos
print(df) # Imprimimos el DataFrame para ver su contenido

# Para guardar el DataFrame en un archivo CSV, puedes usar el método to_csv() de Pandas.
# El siguiente código guarda el DataFrame en un archivo llamado "inventario.csv" en el mismo directorio donde se ejecuta el script:
df.to_csv("inventario.csv", index=False) # Guardamos el DataFrame en un archivo CSV sin incluir el índice   
# El parámetro index=False se utiliza para evitar que se guarde el índice del DataFrame en el archivo CSV.

# Para pder guardar el DataFrame en un archivo Excel, puedes usar el método to_excel() de Pandas.
# El siguiente código guarda el DataFrame en un archivo llamado "inventario.xlsx":
df.to_excel("inventario.xlsx", index=False) # Guardamos el DataFrame en un archivo Excel sin incluir el índice  
# El parámetro index=False se utiliza para evitar que se guarde el índice del DataFrame en el archivo Excel.

# Para poder guardar el DataFrame en un archivo JSON, puedes usar el método to_json() de Pandas.
# El siguiente código guarda el DataFrame en un archivo llamado "inventario.json":
df.to_json("inventario.json", orient="records", lines=True) # Guardamos el DataFrame en un archivo JSON con formato de registros por línea
# El parámetro orient="records" se utiliza para guardar cada fila del DataFrame como un registro JSON independiente, y lines=True se utiliza para escribir cada registro en una línea separada en el archivo JSON.  

# Para poder guardar el DataFrame en un directorio específico, puedes proporcionar la ruta completa del archivo en lugar de solo el nombre del archivo.
# Por ejemplo, si deseas guardar el archivo CSV en un directorio llamado "datos", puedes hacer lo siguiente:
df.to_csv("F:\\PROGRAMING\\PYTHON\\SCode\\Proyectos-Practicos\\inventario.csv", index=False) # Guardamos el DataFrame en un archivo CSV en el directorio "datos" sin incluir el índice
# Asegúrate de que el directorio "datos" exista antes de ejecutar este código, de lo contrario, obtendrás un error. Puedes crear el directorio usando el siguiente código:
os.makedirs("F:\\PROGRAMING\\PYTHON\\SCode\\Proyectos-Practicos\\datos", exist_ok=True) # Crea el directorio "datos" si no existe, y no genera un error si ya existe 

# Para agregar una nueva columna al DataFrame, puedes asignar una lista de valores a una nueva etiqueta de columna.
# Por ejemplo, si deseas agregar una columna llamada "Total" que sea el resultado de multiplicar la cantidad por el precio, puedes hacer lo siguiente:
df["Total:"] = df["Cantidad:"] * df["Precio:"] # Agregamos una nueva columna "Total:" que es el resultado de multiplicar la cantidad por el precio
print(df) # Imprimimos el DataFrame para ver la nueva columna "Total:" agregada

# Para guardar el DataFrame actualizado con la nueva columna "Total:" en un archivo CSV, puedes usar el método to_csv() nuevamente:
df.to_csv("F:\\PROGRAMING\\PYTHON\\SCode\\Proyectos-Practicos\\datos\\inventario_actualizado.csv", index=False) # Guardamos el DataFrame actualizado en un archivo CSV en el directorio "datos" sin incluir el índice   

# Para agregar una nueva columna al DataFrame, donde se pueda calcular el precio con un descuento del 10%, puedes hacer lo siguiente:
df["Precio con Descuento:"] = df["Precio:"] * 0.9 # Agregamos una nueva columna "Precio con Descuento:" que es el resultado de multiplicar el precio por 0.9 (descuento del 10%)
print(df) # Imprimimos el DataFrame para ver la nueva columna "Precio con Descuento:" agregada

# Para guardar el DataFrame actualizado con la nueva columna "Precio con Descuento:" en un archivo Excel, puedes usar el método to_excel() nuevamente:
df.to_excel("F:\\PROGRAMING\\PYTHON\\SCode\\Proyectos-Practicos\\datos\\inventario_actualizado.xlsx", index=False) # Guardamos el DataFrame actualizado en un archivo Excel en el directorio "datos" sin incluir el índice  

# Utilizando un función que luego será llamada para cálcular el precio a moneda de dolares, puedes hacer lo siguiente:
def convertir_a_dolares(precio_en_pesos):
    tasa_de_cambio = 0.05 # Supongamos que 1 peso equivale a 0.05 dólares
    precio_en_dolares = precio_en_pesos * tasa_de_cambio
    return precio_en_dolares

df["Precio en Dólares:"] = df["Precio:"] * 0.05 # Agregamos una nueva columna "Precio en Dólares:" que es el resultado de multiplicar el precio por la tasa de cambio
print(df) # Imprimimos el DataFrame para ver la nueva columna "Precio en Dólares:" agregada 
# Para guardar el DataFrame actualizado con la nueva columna "Precio en Dólares:" en un archivo JSON, puedes usar el método to_json() nuevamente:
df.to_json("F:\\PROGRAMING\\PYTHON\\SCode\\Proyectos-Practicos\\datos\\inventario_actualizado.json", orient="records", lines=True) # Guardamos el DataFrame actualizado en un archivo JSON con formato de registros por línea en el directorio "datos"      

