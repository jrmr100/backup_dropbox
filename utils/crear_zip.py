import os
import zipfile
from utils.logger import logger

def crear_zip(directorio, nombre_zip):
    try:
        logger.info(f"Creando el zip: {nombre_zip}")
        with zipfile.ZipFile(nombre_zip, 'w', zipfile.ZIP_DEFLATED) as archivo_zip:
            for archivo_nombre in os.listdir(directorio):
                archivo_ruta = os.path.join(directorio, archivo_nombre)
                if os.path.isfile(archivo_ruta):  # Asegúrate de que sea un archivo
                    archivo_zip.write(archivo_ruta, archivo_nombre)
        logger.info(f"Se ha creado exitosamente el zip: {nombre_zip}")
    except Exception as e:
        logger.error(f"Except: Error al crear el zip: {e}")