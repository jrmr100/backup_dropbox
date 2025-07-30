
import os
from dotenv import load_dotenv
import glob

load_dotenv()

from utils.logger import logger

def delete_files(ultimo_zip, dias_backup_server):
    try:
        # capturo la carpeta origen
        ruta_origen = os.path.dirname(ultimo_zip)
        # Elimino los archivos fuera del rango a resguardar
        source_files = sorted(glob.glob(os.path.join(ruta_origen, "*")), key=os.path.getmtime,
                               reverse=True)
        if len(source_files) > dias_backup_server:
            for file_to_delete in source_files[dias_backup_server:]:
                if "__init__.py" not in file_to_delete:
                    logger.info(f"Eliminando: {file_to_delete}")
                    os.remove(file_to_delete)
                else:
                    logger.info(f"No se elimino: {file_to_delete}")

        else:
            logger.info(
                f"No se eliminan archivos en la ruta de origen, no hay archivos mas antiguos a {dias_backup_server} dias.")
    except Exception as e:
        logger.error(f"Except al eliminar archivos: {e}")
