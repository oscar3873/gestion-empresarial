import os
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def leer_csv(nombre_archivo):
    ruta_archivo = os.path.join(BASE_DIR, 'static', nombre_archivo)
    try:
        with open(ruta_archivo, 'r', newline='', encoding='utf-8') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            data = []
            for fila in lector_csv:
                data.append(tuple(fila))
            return data
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado en la carpeta 'static'")
    except Exception as e:
        print(f"Error al leer el archivo '{nombre_archivo}': {e}")


def procesar_paises(paises):
    resultado = []
    for pais in paises:
        nombre, _, _, _, _, phone_code = pais
        resultado.append((phone_code, nombre))
    return tuple(resultado)
