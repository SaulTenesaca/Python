import shutil

# Ruta de la carpeta de origen
carpeta_origen = "photos"

# Ruta de la carpeta de destino
carpeta_destino = "copia"

# Copiar todo el contenido de la carpeta de origen a la carpeta de destino
try:
    shutil.copytree(carpeta_origen, carpeta_destino)
    print(f"Se copiaron todos los archivos de '{carpeta_origen}' a '{carpeta_destino}'")
except FileExistsError:
    print(f"La carpeta '{carpeta_destino}' ya existe. No se puede copiar.")
except Exception as e:
    print(f"Ocurrió un error al copiar los archivos: {str(e)}")
