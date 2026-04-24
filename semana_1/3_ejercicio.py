import os
def crear_backup():
    carpeta_backup = "backup"
    archivo_original = "original.txt"
    archivo_copia = os.path.join(carpeta_backup, "copia.txt")
    
    #* Crear la carpeta de backup si no existe
    if not os.path.exists(carpeta_backup):
        os.makedirs(carpeta_backup, exist_ok=True)
        print(f'Carpeta {carpeta_backup} creada')
        
    #* Crear un archivo original de ejemplo al que le hare una copia de seguridad
    if not os.path.isfile(archivo_original):
        #* Crear y Escribir en un archivo.
        with open(archivo_original, 'w', encoding='utf-8') as archivo:
            archivo.write('Este es el contenido del archivo original que debes copiar, con copia de seguridad \n')
        print(f'Archivo {archivo_original} creado')
    
    try:
        #* Copiar el archivo original al destino
        #* READ en un archivo.
        with open(archivo_original, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        
        #* Crear y Escribir en el archivo copia el contenido del orif=ginal.
        with open(archivo_copia, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
            print(f'Archivo del Backup {archivo_copia} fue creado')
    except Exception as e:
        print('Ocurrió un error al crear el backup:', e)

crear_backup()