import os

# Directorio donde se encuentran las imágenes
directorio = './photos'

# Obtener la lista de archivos en el directorio
archivos = os.listdir(directorio)

# Filtrar solo los archivos con extensión .jpg
archivos_jpg = [archivo for archivo in archivos if archivo.endswith('.jpg')]

# Ordenar los archivos por fecha de creación
archivos_jpg.sort(key=lambda archivo: os.path.getctime(os.path.join(directorio, archivo)))

# Invertir el orden de la lista
archivos_jpg = archivos_jpg[::-1]

# Renombrar los archivos con nombres secuenciales
for i, archivo in enumerate(archivos_jpg):
    nuevo_nombre = f'{i + 1}.jpg'
    ruta_antigua = os.path.join(directorio, archivo)
    ruta_nueva = os.path.join(directorio, nuevo_nombre)
    os.rename(ruta_antigua, ruta_nueva)
    print(f'Renombrado: {ruta_antigua} -> {ruta_nueva}')
