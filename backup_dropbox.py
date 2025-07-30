import os
import glob
import shutil
from dotenv import load_dotenv
from utils.dropbox_api import upload_file_dropbox
from utils.file_delete import delete_files

load_dotenv()

from utils.logger import logger, today
from utils.crear_zip import crear_zip

def backup_mw(ruta_origen, ruta_dropbox, dias_backup_server, zip_tmp, system_name):
    # Verificar si el directorio existe
    if not os.path.exists(ruta_origen):
        logger.error(f"{system_name} - Error: El directorio de origen '{ruta_origen}' no existe.")
        return
    try:

        if "uploads" in ruta_origen:
            # Creo el zip de las img si la ruta origen es uploads
            crear_zip(ruta_origen, zip_tmp + system_name + "_img_" + today + ".zip")
            # Obtener el ultimo zip del temporal zip
            ultimo_zip = max(glob.glob(os.path.join(zip_tmp, '*.zip')), key=os.path.getctime)
            logger.info(f"El ultimo zip de {system_name} es: {ultimo_zip}")
        else:
            # Obtener el ultimo zip del origen DB
            ultimo_zip = max(glob.glob(os.path.join(ruta_origen, '*.zip')), key=os.path.getctime)
            logger.info(f"El ultimo zip de {system_name} es: {ultimo_zip}")

        # Subir el archivo a dropbox
        #upload_file = upload_file_dropbox(ultimo_zip, ruta_dropbox)
        upload_file = True

        if upload_file:
            # Eliminar los archivos anteriores al rango configurado
            delete_files(ultimo_zip, dias_backup_server)



    except Exception as e:
        logger.error(f"DB - Except al copiar el archivo: {e}")



# MIKROWISP1_DB
ruta_origen_mw1 = os.getenv("SOURCE_DIR_DB_MW1")
ruta_dropbox_mw1 = os.getenv("DESTINATION_DIR_DB_MW1")
dias_backup_server_mw1 = os.getenv("DIAS_BACKUP_SERVER_MW1")
system_name_mw1 = os.getenv("SYSTEM_NAME_MW1")
zip_tmp_mw1 = os.getenv("ZIP_TMP_MW1")
backup_mw(ruta_origen_mw1, ruta_dropbox_mw1, int(dias_backup_server_mw1), zip_tmp_mw1, system_name_mw1)

# MIKROWISP1_IMG
ruta_origen_mw1 = os.getenv("SOURCE_DIR_IMG_MW1")
ruta_dropbox_mw1 = os.getenv("DESTINATION_DIR_IMG_MW1")
backup_mw(ruta_origen_mw1, ruta_dropbox_mw1, int(dias_backup_server_mw1), zip_tmp_mw1, system_name_mw1)

"""# MIKROWISP2_DB
ruta_origen_mw2 = os.getenv("SOURCE_DIR_DB_MW2w2")
ruta_dropbox_mw2 = os.getenv("DESTINATION_DIR_DB_MW2")
dias_backup_server_mw2 = os.getenv("DIAS_BACKUP_SERVER_MW2")
system_name_mw2 = os.getenv("SYSTEM_NAME_MW2")
zip_tmp_mw2 = os.getenv("ZIP_TMP_MW2")
backup_mw(ruta_origen_mw2, ruta_dropbox_mw2, int(dias_backup_server_mw2), zip_tmp_mw2, system_name_mw2)

# MIKROWISP1_IMG
ruta_origen_mw2 = os.getenv("SOURCE_DIR_IMG_MW2")
ruta_dropbox_mw2 = os.getenv("DESTINATION_DIR_IMG_MW2")
backup_mw(ruta_origen_mw2, ruta_dropbox_mw2, int(dias_backup_server_mw2), zip_tmp_mw2, system_name_mw2)"""


# TODO: Obtener TOKEN de dropbox
# TODO: Crear funcion de proxmox
# TODO: Eliminar historico de dropbox - solo lo definido en .env
