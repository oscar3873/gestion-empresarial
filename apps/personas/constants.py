from utils.services_csv import leer_csv, procesar_paises

GENERO_CHOICES = (('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro'))
# Lee y procesa los países del archivo paises.csv y los convierte en una tupla de tuplas con el formato (código, nombre)
COD_PAISES = procesar_paises(leer_csv('paises.csv'))
# Calcula el tamaño máximo de los códigos de país
MAX_COD_PAIS_LENGTH = max(len(cod_pais) for cod_pais, nombre in COD_PAISES)
