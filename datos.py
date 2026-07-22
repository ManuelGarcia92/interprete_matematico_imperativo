import json
import os

def ruta_actual(nombre_archivo):
    carpeta_actual = os.path.dirname(__file__)
    ruta_actual = os.path.join(carpeta_actual, nombre_archivo)
    return ruta_actual

def cargar_datos(ruta):
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []

def guardar_datos(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)



