import shutil

# Ruta de la carpeta que deseas eliminar
carpeta_a_eliminar = "copia"  # Cambia esto por la ruta de la carpeta que deseas eliminar

try:
    # Eliminar la carpeta y su contenido de manera recursiva
    shutil.rmtree(carpeta_a_eliminar)
    print(f"Se eliminó la carpeta '{carpeta_a_eliminar}' y su contenido exitosamente")
except FileNotFoundError:
    print(f"La carpeta '{carpeta_a_eliminar}' no existe")
except Exception as e:
    print(f"Ocurrió un error al eliminar la carpeta: {str(e)}")
