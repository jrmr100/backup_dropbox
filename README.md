# nombre_proyecto
    backup_dropbox

# Objetivo:
Realizar respaldo de Mikrowisp1 y 2, Proxmox y cualquier archivo a DROPBOX

# Premisas
    - Dias de respaldo configurable
    - comprimir las imagenes upload de mikrowisp
    - Dejar dos respaldos en el server para ahorrar espacio
    - Ejecutar a las 5 am de la mañana todos los dias

# Algoritmo
    - Identificar las ruta de los archivos fuentes a respaldar y las de dropbox y agregarlas al .env
    - Leer el origen, Si es un archivo comprimido seleccionar el ultimo, en caso contrario crear un zip
    - Validar que el zip no exista en el dropbox 
    - En caso que no exista subir el archivo a dropbox
    - Dejar en el server solo los dos ultimos respaldos
    - Eliminar de dropbox todos los archivos anteriores al rango configurado

# INSTALACIÓN:
- Sistema base: Debian 12
- Actualizar los repositorios del sistema

      sudo apt install git virtualenv nfs-common

- Clonar el repositorio de github
- Crear entorno virtual de python dentro de la carpeta root del proyecto

      virtualenv .venv -p /usr/bin/python3
      source .venv/bin/activate
- Crear la aplicacion en dropbox, otorgar los permisos y generar el token

      https://www.dropbox.com/developers
      nombre: backup_IFX
      Carpetas: Mikrowisp1, Mikrowisp2, Proxmox 

- Instala los requerimientos del sistema

      .venv/bin/pip3 install -r requirements.txt

- Configurar .env con los datos y rutas del sistema

- Cambiar el propietario de toda la carpeta en caso de producción

      sudo chown -R jmonroy:jmonroy backup_mw
- Crear un crontab para Ejecutar el script
      
        De forma local: 
        .venv/bin/python3 backup_mw.py
        
        Desde crontab:
        sudo crontab -e
        0 4 * * * cd /home/jmonroy/python/backup_mw && .venv/bin/python3 backup_mw.py 

- TROUBLESHOOTING

      - Revisar la carpeta log
      - en utils/zip_img se guarda el archivo .zip de las imagenes 
        